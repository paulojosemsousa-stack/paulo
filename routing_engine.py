from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def optimize_routes(orders):
    """
    Motor OR-Tools para separação de carga e roteirização.
    Resolve o Vehicle Routing Problem (VRP) com restrição de cubagem/peso.
    """
    # Matriz simplificada do eixo BR-163 (CD -> Cuiabá -> Nova Mutum -> LRV -> Sinop)
    distance_matrix = [
        [0, 240, 330, 400, 480],
        [240, 0, 90, 160, 240],
        [330, 90, 0, 70, 150],
        [400, 160, 70, 0, 80],
        [480, 240, 150, 80, 0],
    ]
    
    demands = [0] + [order["peso"] for order in orders]
    vehicle_capacities = [8000, 8000] # 2 caminhões de 8 Toneladas
    
    manager = pywrapcp.RoutingIndexManager(len(distance_matrix), len(vehicle_capacities), 0)
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    def demand_callback(from_index):
        return demands[manager.IndexToNode(from_index)]

    demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
    routing.AddDimensionWithVehicleCapacity(demand_callback_index, 0, vehicle_capacities, True, 'Capacity')

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    
    solution = routing.SolveWithParameters(search_parameters)
    
    if not solution:
        return {"status": "error", "message": "Sem solução para a capacidade atual."}

    return {"status": "success", "message": "Rotas otimizadas com sucesso.", "distancia_total": solution.ObjectiveValue()}