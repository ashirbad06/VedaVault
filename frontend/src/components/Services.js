import React from 'react';

function Services() {
  return (
    <div className="container">
      <h1>Our Services</h1>
      <div className="row">
        <div className="col-md-4">
          <h2>Basic Plan</h2>
          <p>Includes fundamental strategies and access to resources.</p>
          <p>Price: $10/month</p>
        </div>
        <div className="col-md-4">
          <h2>Standard Plan</h2>
          <p>Includes advanced strategies, personalized services, and analytics.</p>
          <p>Price: $20/month</p>
        </div>
        <div className="col-md-4">
          <h2>Premium Plan</h2>
          <p>Complete access to all services, 24/7 support, and priority services.</p>
          <p>Price: $50/month</p>
        </div>
      </div>
    </div>
  );
}

export default Services;
