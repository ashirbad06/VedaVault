import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Resources() {
  const [resources, setResources] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/resources')
      .then(res => setResources(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="container">
      <h1>Resources</h1>
      <ul>
        {resources.map(resource => (
          <li key={resource.id}>
            <a href={resource.link}>{resource.title}</a>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Resources;
