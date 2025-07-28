from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

class OptimizationService:
    @staticmethod
    def optimize_route(locations, distance_matrix):
        """Solve TSP using Google OR-Tools"""
        # Create routing index manager
        manager = pywrapcp.RoutingIndexManager(len(locations), 1, 0)
        
        # Create distance matrix
        def distance_callback(from_index, to_index):
            from_node = manager.IndexToNode(from_index)
            to_node = manager.IndexToNode(to_index)
            return distance_matrix[from_node][to_node]

        routing = pywrapcp.RoutingModel(manager)
        transit_callback_index = routing.RegisterTransitCallback(distance_callback)
        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

        # Solve
        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

        solution = routing.SolveWithParameters(search_parameters)
        return solution
