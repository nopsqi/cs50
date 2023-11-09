const Profile = () => {
    const [state, setState] = React.useState({
        url: new URL(window.location.pathname, window.location.origin)
    })
    return (
        <div>
            THIS IS PROFILE
        </div>
    )
}

ReactDOM.render(<Profile />, document.querySelector('#profile'));
