import { useForm } from "react-hook-form";

const HookForm = () => {
    const { register, handleSubmit } = useForm();

    const onSubmit = (data) => {
        console.log(data);
    };

    return (
        <div className="m-5 w-1/2 mx-auto">
            <form onSubmit={handleSubmit(onSubmit)}>
                <div className="mb-3">
                    <label className="block text-gray-700 text-sm font-bold mb-2"
                        htmlFor="name"
                    >
                        Name:
                    </label>
                    <input
                        {...register("name")}
                        id = "name"
                        type="text"
                        className="w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 rounded-md"
                    />
                </div>
                <div className="mt-3 mb-3">
                    <label className="block text-gray-700 text-sm font-bold mb-2"
                        htmlFor="age"
                    >
                        Age:
                    </label>
                    <input
                        {...register("age")}
                        id = "age"
                        type="number"
                        className="w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 rounded-md"
                    />
                </div>
                <button className="px-3 py-2 bg-blue-500 text-white rounded-md mt-2">
                    Submit
                </button>
            </form>
        </div>
    );
};

export default HookForm;