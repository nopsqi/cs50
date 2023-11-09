const Profile = () => {
    const [state, setState] = React.useState({
        username: new URL(window.location.pathname, window.location.origin).pathname.slice(1)
    })

    React.useEffect(() => {
        fetch(`/user?username=${state.username}`)
        .then(response => response.json())
        .then(result => {
            setState(result)
        })
    }, [])
    console.log(state)

    return (
        <div className="card-body">
            <a href="">{state.username}</a>
        </div>
    )
}

ReactDOM.render(<Profile />, document.querySelector('#profile'));
