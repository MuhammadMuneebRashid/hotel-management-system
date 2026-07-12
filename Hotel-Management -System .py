# Room class stores the details of a single room
class Room:
# Constructors to initialize room details
    def __init__(self,room_no,room_type,price):
        self.room_no=room_no
        self.room_type=room_type
        self.price=price
        self.booked=False
    # Book the room if it is available
    def book_room(self):
        if self.booked:
            print("Room is already book")
        else:
            self.booked=True
            print("Room booked successfully")
    # Cancel the booking of a room
    def cancel_booking(self):
        if self.booked:
            self.booked=False
            print("Booking is cancelled")
        else:
            print("Room is not booked")
    # Display room information
    def display_info (self):
        if self.booked:
            status="booked"
        else:
            status="Available"
        print(f"Room_No: {self.room_no}")
        print(f"Room_type: {self.room_type}")
        print(f"Price: {self.price}")
        print(f"Status: {status}")
        print("-"*20)
# Hotel class manages all rooms
class Hotel:
    # constructor to create an empty list of rooms
    def __init__(self):
        self.rooms=[]
    # Add new room
    def add_room(self):
         room_no=int(input("Enter the room number:"))
         room_type=input("Enter the room type:")
         price=int(input("Enter the price of room:"))
         room=Room(room_no,room_type,price)
         self.rooms.append(room)
         print("Room added successfully")
    # Display all available rooms
    def show_available_rooms(self):
        found=False
        for room in self.rooms:
            if not room.booked:
                room.display_info()
                found=True
        if not found:
            print("Rooms are not available")
    # Book a room using room number
    def book_room(self):
        room_num=int(input("Enter the room number:"))
        for room in self.rooms:
            if room.room_no==room_num:
                room.book_room()
                break
        else:   
            print("Room not found")
    # Cancel a room booking
    def cancel_booking(self):
        room_num=int(input("Enter the room number:"))
        for room in self.rooms:
            if room.room_no==room_num:
                room.cancel_booking()
                break
        else:
                 print("Room not found")
# Create a Hotel object
hotel=Hotel()
# Main Menu of the Hotel Management System
while True:
    print("=== Hotel Management System ===")
    print("1. Add Room")
    print("2. Show Available Room")
    print("3. Book Room")
    print("4. Cancel Booking")
    print("5. Exit")
    choice=int(input("enter the choice:"))
    if(choice==1):
        hotel.add_room()
    elif(choice==2):
        hotel.show_available_rooms()
    elif(choice==3):
        hotel.book_room()
    elif(choice==4):
        hotel.cancel_booking()
    elif(choice==5):
        print("Thankyou for your reservation of a room")
        break
    # Handles Invalid Input
    else:
        print("Invalid choice")
        
                


        