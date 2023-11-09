const Profile = () => {
    const [state, setState] = React.useState({
        url: new URL(window.location.pathname, window.location.origin)
    })

    React.useEffect(() => {
        fetch()
    }, [])

    return (
        <div className="card">
            <div className="card-body"></div>
        </div>
    )
}

ReactDOM.render(<Profile />, document.querySelector('#profile'));
