import { useEffect, useState } from 'react';

const Effect = () => {
    const [users, setUsers] = useState([]);
    const [dependancyA, setDependanceyA] = useState(0);
    const [dependancyB, setDependanceyB] = useState(0);

    useEffect(() => {
        console.log("Effect occured");
        
        if (users.length === 0) {
            setUsers(["Hasan"]);
        }
    }, [dependancyA, dependancyB]);

    return (
        <div>
            <h1>UserList</h1>
            <button
                onClick={() => setDependanceyA(Math.random())}
                className='px-3 py-2 bg-blue-500 text-white me-2'
            >
                Click Me A
            </button>        
            <button
                onClick={() => setDependanceyB(Math.random())}
                className='px-3 py-2 bg-blue-500 text-white'
            >
                Click Me B
            </button>        
        </div>
    );
};

export default Effect;

/*
Side Effects
    1. Manually modify the DOM
    2. Store data in local storage
    3. Call the to fetch/save data
*/