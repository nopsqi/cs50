const App = () => {
    const [state, setState] = React.useState({
        new_post: {
            value: 0
        }
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
    console.log("on new posts", props)

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
