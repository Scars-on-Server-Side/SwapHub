function StartThing(props) {

    return (
        <li className="StartItem col mb-4">
            <div className="card h-100">
                <img src={props.img} alt={props.name} />
                <div className="card-footer">
                    <small className="text-body-secondary">{props.name}</small>
                </div>
            </div>
        </li>
    );
}

export default StartThing;
