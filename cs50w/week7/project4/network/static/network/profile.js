const Profile = () => {
    const [state, setState] = React.useState({
        user: new URL(window.location.pathname, window.location.origin).pathname.slice(1)
    })

    React.useEffect(() => {
        fetch(`/user?username=${state.user}`)
        .then(response => response.json())
        .then(result => {
            console.log(result)
        })
    }, [])

    return (
        <div className="card mt-3">
            <div className="card-body"></div>
        </div>
    )
}

ReactDOM.render(<Profile />, document.querySelector('#profile'));
