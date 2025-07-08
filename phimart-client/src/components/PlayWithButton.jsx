import { useState } from 'react';
import Alert from './Alert';
import Button from './Button';

const PlayWithButton = () => {
    const handleClick = () => console.log("Button Clicked");

    const [alertVisible, setAlertVisible] = useState(false);

    return (
        <div>
            {alertVisible && (
                <Alert color="success">You have clicked the oneSix Button</Alert>
            )}
            <Button handleClick={() => setAlertVisible(true)}>
                Click Me
            </Button>
        </div>
    );
};

export default PlayWithButton;