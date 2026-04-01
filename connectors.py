import random

class ERPConnectors:
    """Simula as chamadas aos bancos e APIs dos ERPs (Winthor, SAP, Sankhya, Protheus)"""
    @staticmethod
    def get_all_orders():
        return [
            {"numped": "WNT-1001", "origem": "Winthor", "cliente": "Inpasa", "peso": 3500, "receita": 18500, "lat": -12.518, "lng": -55.719, "cidade": "Sinop / MT"},
            {"numped": "SAP-2099", "origem": "SAP B1", "cliente": "3 Tentos", "peso": 2000, "receita": 12000, "lat": -13.832, "lng": -56.072, "cidade": "Nova Mutum / MT"},
            {"numped": "SNK-3042", "origem": "Sankhya", "cliente": "Fazenda Alvorada", "peso": 4500, "receita": 22000, "lat": -13.067, "lng": -55.908, "cidade": "Lucas do Rio Verde / MT"},
            {"numped": "PRT-4010", "origem": "Protheus", "cliente": "Agropecuária Sul", "peso": 1500, "receita": 8900, "lat": -15.601, "lng": -56.097, "cidade": "Cuiabá / MT"}
        ]

class FleetCostConnectors:
    """Integração com gestão de frota, manutenção e despesas de viagem"""
    @staticmethod
    def get_ticketlog_costs(placa):
        # Simula API Ticket Log (Abastecimento, Peças, Oficina)
        base_diesel = random.uniform(3000, 5000)
        manutencao = random.uniform(500, 1500)
        return {
            "placa": placa,
            "fornecedor_cartao": "ValeCard / TicketLog",
            "combustivel_diesel": round(base_diesel, 2),
            "manutencao_oficina": round(manutencao, 2),
            "total_ticketlog": round(base_diesel + manutencao, 2)
        }

    @staticmethod
    def get_vexpense_costs(placa):
        # Simula API VExpense (Despesas do Motorista, Alimentação, Pedágio, Chapa)
        pedagio = random.uniform(400, 800)
        alimentacao_estadia = random.uniform(300, 700)
        return {
            "placa": placa,
            "pedagios": round(pedagio, 2),
            "reembolsos_viagem": round(alimentacao_estadia, 2),
            "total_vexpense": round(pedagio + alimentacao_estadia, 2)
        }