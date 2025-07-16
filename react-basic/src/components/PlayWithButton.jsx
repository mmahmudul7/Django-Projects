import { useState } from 'react';
import Alert from './Alert';
import Button from './Button';

const PlayWithButton = () => {
    const [alertVisible, setAlertVisible] = useState(false);

    return (
        <div>
            {alertVisible && (
                <Alert color="success" onClose={() => setAlertVisible(false)}>
                    You have clicked the oneSix Button
                </Alert>
            )}
            <Button className="font-extrabold"
            handleClick={() => setAlertVisible(true)}>
                oneSix
            </Button>
        </div>
    );
};

export default PlayWithButton;