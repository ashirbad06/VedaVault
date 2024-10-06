import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Team() {
  const [members, setMembers] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/team')
      .then(res => setMembers(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="container">
      <h1>Meet Our Team</h1>
      <div className="row">
        {members.map(member => (
          <div key={member.id} className="col-md-4">
            <img src={member.photo_url} alt={member.name} />
            <h2>{member.name}</h2>
            <p>{member.position}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Team;
