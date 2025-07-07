// First Comment 
// PascalCasing 
const FirstComponent = () => {
    const name = "Phitron"

    const sum = (a, b) => a + b;

    return (
        <>
            <h1>Hello {name && "World!"}</h1>
            <h1>Hello {name || "World!"}</h1>
            <p>Your mark is {sum(5, 34)}</p>
        </>
    );
};

export default FirstComponent;