#!/usr/bin/env python3
import argparse
from mpi4py import MPI


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


class MPIExamples:
    @staticmethod
    def basicc_comm() -> None:
        """Basic blocking communication between nodes"""
        pass

    @staticmethod
    def broadcast_comm() -> None:
        """Broadcast data to all nodes in your network"""
        pass

    @staticmethod
    def scatter_comm() -> None:
        """Scatter an array"""
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--example-one", action="store_true", help="Run example 1")
    parser.add_argument("--example-two", action="store_true", help="Run example 2")
    parser.add_argument("--example-three", action="store_true", help="Run example 3")
    args = parser.parse_args()

    if args.example_one:
        MPIExamples.basicc_comm()

    elif args.example_two:
        MPIExamples.broadcast_comm()

    elif args.example_three:
        MPIExamples.scatter_comm()
