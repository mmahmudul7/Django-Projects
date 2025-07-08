const Button = ({ handleClick, children, color = "success" }) => {
    const BtnColors = {
        primary: "bg-blue-500",
        success: "bg-green-500",
        danger: "bg-red-500",
        warning: "bg-yellow-500",
        info: "bg-cyan-500",
    };

    return (
        <button
            onClick={handleClick}
            className={`m-5 px-3 py-2 bg-blue-500 text-white rounded-sm ${BtnColors[color]}`}
        >
            {children}
        </button>
    );
};

export default Button;