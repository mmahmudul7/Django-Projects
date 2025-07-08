import { useState } from "react";

const Alert = ({ color = 'info', children }) => {
    const [visible, setVisible] = useState(true);

    const alertStyle = {
        success: "bg-green-100 text-green-800 border border-green-300",
        error: "bg-red-100 text-red-800 border border-red-300",
        warning: "bg-yellow-100 text-yellow-800 border border-yellow-300",
        info: "bg-blue-100 text-blue-800 border border-blue-300",
    };

    if (!visible) return null;

    return (
        <div className={`flex items-center justify-between rounded-sm p-4 ${alertStyle[color]}`}>
            <span>{children}</span>
            <button onClick={() => setVisible(false)}>x</button>
        </div>
    );
};

export default Alert;