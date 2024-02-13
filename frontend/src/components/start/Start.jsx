import StartThing from "./StartThing";


function Start(props) {
    const startThings = props.startThings

    return (
        <ul className="Start row row-cols-1 row-cols-md-3 g-4 m-3">
            {startThings.map((thing, index) => (
                <StartThing key={index} img={thing.img} name={thing.name} />
            ))}
        </ul>
    )
}

export default Start;
