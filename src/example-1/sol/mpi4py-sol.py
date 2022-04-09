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
        if rank == 0:
            data = "Hello there"
            if size == 2:
                comm.send(data, dest=1, tag=1)

            if size == 3:
                comm.send(data, dest=2, tag=2)
            
            if size == 4:
                comm.send(data, dest=3, tag=3)

            if size >= 2:
                res = comm.recv(source=1, tag=4)
                print(f"{res} from node {rank}")

        elif rank == 1:
            data = comm.recv(source=0, tag=1)
            print(f"{data} from node {rank}")
            comm.send("General Kenobi", dest=0, tag=4)

        elif rank == 2:
            data = comm.recv(source=0, tag=2)
            print(f"{data} from node {rank}")

        elif rank == 3:
            data = comm.recv(source=0, tag=3)
            print(f"{data} from node {rank}")

    @staticmethod
    def broadcast_comm() -> None:
        """Broadcast data to all nodes in your network"""
        if rank == 0:
            data = {"message1": "Hello there", "message2": "General Kenobi"}

        else:
            data = None
        
        data = comm.bcast(data, root=0)
        print(f"{data['message1']} from node {rank}")
        print(f"{data['message2']} from node {rank}")

    @staticmethod
    def scatter_comm() -> None:
        """Scatter an array"""
        if rank == 0:
            data = [(i+1)**2 for i in range(size)]

        else:
            data = None

        data = comm.scatter(data, root=0)
        print(f"{data} from node {rank}")


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
