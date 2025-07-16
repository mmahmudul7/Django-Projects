import { useState } from 'react';

const Employee = () => {
    const employeeArr = [
        { name: "Mahmud", age: 20 },
        { name: "Hasan", age: 15 },
    ];
    const [employee, setEmployee] = useState(employeeArr);

    const handleClick = () => {
        setEmployee(
            employee.map(
                (emp) => (emp.name === "Mahmud" ? { ...emp, age: 60 } : emp)
            )
        );
    };

    return (
        <div className='m-5'>
            <ul className='list-disc m-5'>
                {employee.map((emp, index) => (
                    <li key={index}>
                        Name: {emp.name} age: {emp.age}
                    </li>
                ))}
            </ul>
            <button
                onClick={handleClick}
                className='px-3 py-2 bg-green-800 hover:bg-green-700 text-white rounded-md'
            >
                Click to update age
            </button>
        </div>
    );
};

export default Employee;