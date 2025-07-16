import { useRef } from "react";

const Form = () => {
    const nameRef = useRef(null);
    const ageRef = useRef(null);

    const person = { name: "", age: 0 };

    const handleSubmit = (event) => {
        event.preventDefault();
        if (nameRef.current != null) person.name = nameRef.current.value;
        if (ageRef.current != null) person.age = parseInt(ageRef.current.value);
        // console.log(nameRef.current.value);
        console.log(person);
    };

    return (
        <div className="m-5">
            <form onSubmit={handleSubmit}>
                <div className="mb-3">
                    <label className="block text-gray-700 text-sm font-bold mb-2"
                        htmlFor="name"
                    >
                        Name:
                    </label>
                    <input
                        ref={nameRef}
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
                        ref={ageRef}
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

export default Form;