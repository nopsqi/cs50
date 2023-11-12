const Profile = () => {
    const [state, setState] = React.useState({
        loading: true,
        username: document.location.pathname.slice(1)
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

    const toggleFollow = (e) => {
        fetch('/api/user', {
            method: 'PUT',
            body: JSON.stringify({
                id: state.id
            })
        })
    }

    return (
        <div className="mt-3">
            <div className="d-flex justify-content-between">
                <h3><a className="card-title" href="">{state.username}</a></h3>
                {
                    state.is_mine
                    ? ''
                    : <button className={`btn ${state.is_follow ? "btn-secondary" : "btn-primary"}`} onClick={toggleFollow}>Follow</button>
                }
            </div>
            <div className="d-flex">
                <div className="card-text" >Following {state.followings_length}</div>
                <div className="ml-4" >Follower {state.followers_length}</div>
            </div>
        </div>
    )
}

ReactDOM.render(<Profile />, document.querySelector('#Profile'));
