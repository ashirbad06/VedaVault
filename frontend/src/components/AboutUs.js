import React, { useEffect, useState } from 'react';

const AboutUs = () => {
    const [aboutInfo, setAboutInfo] = useState({});

    useEffect(() => {
        const fetchAboutInfo = async () => {
            const response = await fetch('/api/about');
            const data = await response.json();
            setAboutInfo(data);
        };

        fetchAboutInfo();
    }, []);

    return (
        <div>
            <h2>About Us</h2>
            <h3>Mission Statement</h3>
            <p>{aboutInfo.mission}</p>
            <h3>Vision</h3>
            <p>{aboutInfo.vision}</p>
            <h3>Core Values</h3>
            <ul>
                {aboutInfo.core_values && aboutInfo.core_values.map((value, index) => (
                    <li key={index}>{value}</li>
                ))}
            </ul>
        </div>
    );
};

export default AboutUs;
