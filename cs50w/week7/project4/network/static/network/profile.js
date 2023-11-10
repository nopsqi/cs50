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
                followings_length: result.followings.length,
                followers_length: result.followers.length,
                loading: false,
            })
        })
    }, [])

    if (state.loading) {
        return (<div></div>)
    }

    console.log(state)

    return (
        <div className="card-body">
            <div className="d-flex">
                <a href="">{state.username}</a>
                <div className="ml->Following {state.followings_length}</div>
            </div>
        </div>
    )
}

ReactDOM.render(<Profile />, document.querySelector('#profile'));
