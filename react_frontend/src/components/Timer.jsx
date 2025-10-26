import '../styles/timer.css';
import { useEffect, useState } from "react";

const Timer = () => {
    const [days, setDays] = useState(0);
    const [hours, setHours] = useState(0);
    const [minutes, setMinutes] = useState(0);
    const [seconds, setSeconds] = useState(0);

    const deadline = "April 4 2026";

    const getTime = () => {
        const time = Date.parse(deadline) - Date.now();

        setDays(Math.floor(time / (1000 * 60 * 60 * 24)));
        setHours(Math.floor((time / 1000 / 60) % 60));
        setMinutes(Math.floor((time / 1000 / 60) % 60));
        setSeconds(Math.floor((time / 1000) % 60));
    };

    useEffect( () => {
        const interval = setInterval(() => getTime(deadline), 1000);
        return () => clearInterval(interval);
    }, []);

    return (
        <div>
            <h1 className='countdown-text'>Countdown Until EOH</h1>
            <div className='container'> 
                <div>
                    <div className='timer-text'>{days}</div> 
                    Days
                </div>
                <div>
                    <div className='timer-text'>{hours}</div> 
                    Hours 
                </div>
                
                <div>
                    <div className='timer-text'>{minutes}</div>
                    Minutes 
                </div>

                <div>
                    <div className='timer-text'>{seconds}</div>
                    Seconds
                </div>
            </div>
        </div>
    ) 
};

export default Timer;