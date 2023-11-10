const Profile = () => {
    const [state, setState] = React.useState({
        loading: true,
        username: new URL(window.location.pathname, window.location.origin).pathname.slice(1)
    })

    React.useEffect(() => {
        fetch(`/api/user?username=${state.username}`)
        .then(response => response.json())
        .then(result => {
            setState({
                ...state,
                ...result,
                loading: false,
            })
        })
    }, [])

    if (state.loading) {
        return (<div></div>)
    }

    return (
        <div className="card-body">
            <div className="d-flex">
                <a href="">{state.username}</a>
                <div>Following</div>
            </div>
        </div>
    )
}

ReactDOM.render(<Profile />, document.querySelector('#profile'));
