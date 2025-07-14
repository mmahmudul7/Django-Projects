import { Trash2 } from "lucide-react";
import { useForm } from "react-hook-form";

const CartApp = () => {
    const { register, handleSubmit } = useForm();

    const cart = [
        {name: "Laptop", price: 34000},
        {name: "Mobile", price: 25000},
    ];

    const addItem = (data) => {
        console.log(data);
    }

    return (
        <div className="w-2/3 mx-auto bg-gray-100 rounded-lg p-6 shadow-md">

            {/* Add Cart Items  */}
            <form onSubmit={handleSubmit(addItem)} className="mb-4 space-y-2">
                <input {...register("name", { required:true })} type="text" placeholder="Item Name" className="border p-2 rounded w-full" />
                <input {...register("price", { required:true })} type="number" placeholder="Item Price" className="border p-2 rounded w-full" />
                <button className="bg-blue-500 text-white px-4 py-2 rounded w-full">Add Item</button>
            </form>

            {/* Cart Items List  */}
            {cart.length > 0 ?(
                // Todo cart items 
                <div>
                    {cart.map(item => (
                        <div key={item.name} className="flex justify-between items-center p-2 bg-white rounded mb-2">
                            <p className="font-semibold">{item.name}</p>
                            <p className="text-sm text-gray-600">{item.price}</p>

                            <div className="flex items-center">
                                <button className="bg-red-500 text-white px-2 py-1 rounded">-</button>
                                <span className="mx-2">1</span>
                                <button className="bg-green-500 text-white px-2 py-1 rounded">+</button>
                            </div>

                            <button><Trash2 /></button>
                        </div>
                        
                    ))}

                    {/* Total Price  */}
                    <div className="mt-4 font-bold text-lg">Total: 41000</div>
                </div>
            ) : (
                <p>No Cart Items</p>
            )}
        </div>
    );
};

export default CartApp;