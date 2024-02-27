import React from "react";

function StartThing(props) {
    const { img, name } = props;

  return (
    <div className="StartThing">
      <img src={img} alt={name} className="image" />
      <div className="overlay">
        <div className="text">{name}</div>
      </div>
    </div>
  );
}

export default StartThing;
