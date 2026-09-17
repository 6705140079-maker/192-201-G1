from rental import Vehicle, Renter, ElectricCar, Motorbike

def main():
    print("--- 1. Basic Vehicle & Renter Demo ---")
    car = Vehicle("Toyota", "Yaris", "1AB234")
    renter = Renter("Alice Smith", 98765)
    
    print(f"Created Renter: {renter.name}")
    print(f"Status before renting: {car}")
    
    car.rent()
    print(f"Status after renting:  {car}")
    
    car.return_vehicle()
    print(f"Status after return:   {car}\n")

    print("--- 2. Encapsulation (Validation) Demo ---")
    try:
        bad_renter_name = Renter("", 12345)
    except ValueError as e:
        print(f"Caught expected error (Empty Name): {e}")

    try:
        bad_renter_license = Renter("Bob Jones", -10)
    except ValueError as e:
        print(f"Caught expected error (Negative License): {e}")
    
    print()

    print("--- 3. Inheritance & Polymorphism Demo ---")
    fleet = [
        Vehicle("Honda", "Civic", "XYZ-999"),
        ElectricCar("Tesla", "Model 3", "EV-123", 75),
        Motorbike("Yamaha", "MT-07", "M-456", 689)
    ]

    fleet[1].rent()

    for vehicle in fleet:
        print(vehicle)

if __name__ == "__main__":
    main()
