company_name = input()
adult_tickets = int(input())
children_tickets = int(input())
neto_ticket_price = float(input())
services = float(input())
children_tickets_price = 0.3 * neto_ticket_price
ticket = services + neto_ticket_price
children_tickets_price_service = services + children_tickets_price
total_tickets = (children_tickets * children_tickets_price_service) + (adult_tickets * ticket)
profit = 0.2 * total_tickets
print(f"The profit of your agency from {company_name} tickets is {profit:.2f} lv.")