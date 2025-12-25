def tower_of_hanoi(n, source, destination, auxiliary):
    if n > 0:
        tower_of_hanoi(n - 1, source, auxiliary, destination)
        print(f"Move disk {n} from {source} to {destination}")
        tower_of_hanoi(n - 1, auxiliary, destination, source)


n = 3
source = "A"
destination = "C"
auxiliary = "B"


print(f"solving tower of Hanoi with {n} disks:")
tower_of_hanoi(n, source, destination, auxiliary)
