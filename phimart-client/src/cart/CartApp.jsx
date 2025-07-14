import { useForm } from "react-hook-form";

const CartApp = () => {
    const { register, handleSubmit } = useForm();

    const addItem = (data) => {
        console.log(data);
    }

    return (
        <div className="w-2/3 mx-auto bg-gray-100 rounded-lg p-6 shadow-md">
            <form onSubmit={handleSubmit(addItem)} className="mb-4 space-y-2">
                <input {...register("name", { required:true })} type="text" placeholder="Item Name" className="border p-2 rounded w-full" />
                <input {...register("price", { required:true })} type="number" placeholder="Item Price" className="border p-2 rounded w-full" />
                <button className="bg-blue-500 text-white px-4 py-2 rounded w-full">Add Item</button>
            </form>
        </div>
    );
};

export default CartApp;