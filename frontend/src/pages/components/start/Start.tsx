import StartThing from "./StartThing.tsx";
import React from "react";


function Start(props) {
  const startThings = props.startThings;


  return (
    <div className="Start">
      {startThings.map((thing, index) => (
        <StartThing
          key={index}
          img={`${thing.avatar}`}
          name={thing.name}
        />
      ))}
    </div>
  );
}

export default Start;
