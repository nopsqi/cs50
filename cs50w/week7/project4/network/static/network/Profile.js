const Profile = () => {
    const [state, setState] = React.useState({
        api: new URL(document.getElementById('Profile').dataset.api, document.location.origin),
        loading: true,
        fetch: true
    })

    React.useEffect(() => {
        setState({
            ...state,
            loading: true
        })

        fetch(state.api)
        .then(response => response.json())
        .then(result => {
            console.log(state)
            console.log(result)
            setState({
                ...state,
                ...result,
                followings_length: result.followings.length,
                followers_length: result.followers.length,
                loading: false,
            })
        })
    }, [state.api, state.fetch])

    if (state.loading) {
        return (<div></div>)
    }

    const toggleFollow = (e) => {
        fetch('/api/user', {
            method: 'PUT',
            body: JSON.stringify({
                id: state.id,
                is_follow: state.is_follow
            })
        })
        .then(response => {
            if (response.status === 200) {
                response.json()
                .then(result => {
                    setState({
                        ...state,
                        ...result
                    })
                })
            }
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
