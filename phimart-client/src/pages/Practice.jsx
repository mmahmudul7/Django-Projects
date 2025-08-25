import { useState } from 'react';

const Practice = () => {
    // const count = 0;
    const [count, setCount] = useState(0);

    // function increment() {
    //     setCount(count + 1);
    // }

    // () => setCount(count + 1);

    return (
        <div className="p-6 flex gap-6 items-center">
            <p>Count: {count}</p>
            <button
                onClick={() => setCount(count + 1)}
                className="btn btn-secondary"
            >
                Click Me
            </button>
        </div>
    );
};

export default Practice;
