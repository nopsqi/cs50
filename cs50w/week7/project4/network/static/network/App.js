const App = () => {
    const [state, setState] = React.useState({
        api: new URL(document.getElementById('App').dataset.api, document.location.origin)
        posts: []
    })

    return (
        <div>
            <NewPost />
            <Posts />
            <Paginator />
        </div>
    )
}

const NewPost = (props) => {
    return (
        <div>
            <h1>NEW POST HOLDER</h1>
        </div>
    )
}

const Posts = () => {
    return (
        <div>
            <h1>POSTS HOLDER</h1>
        </div>
    )
}

const Paginator = () => {
    return (
        <div>
            <h1>PAGINATOR HOLDER</h1>
        </div>
    )
}

ReactDOM.render(<App />, document.getElementById('App'))
