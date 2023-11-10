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
                <h3><a className="card-title" href="">{state.username}</a></h3>
                {
                    state.is_mine
                    ? ''
                    : <button className={`btn ${state.is_follow ? "btn-secondary" : "btn-primary"}`}>Follow</button>
                }
            </div>
            <div className="d-flex">
                <div className="card-text" >Following {state.followings_length}</div>
                <div className="ml-4" >Follower {state.followers_length}</div>
            </div>
        </div>
    )
}

ReactDOM.render(<Profile />, document.querySelector('#profile'));
