import { useState } from "react";

const Person = () => {
    const [person, setPerson] = useState("")
    // const [visible, setVisible] = useState(false)

    const handleClick = () => {
        setPerson("Mahmud");
        console.log(person);
    };
    console.log(person);

    return (
        <div className="m-5">
            <button
                onClick={handleClick}
                className='px-3 py-2 bg-blue-500 text-white rounded-sm'
            >
                Click Me
            </button>            
        </div>
    );
};

export default Person;