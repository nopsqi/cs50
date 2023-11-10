const App = () => {
    const [state, setState] = React.useState({
        api: new URL(document.getElementById('App').dataset.api, document.location.origin),
        posts: [1, 2,]
    })

    const addPost = () => {
        setState({
            ...state,
            posts: [...state.posts, state.posts[state.posts.length-1] + 1]
        })
    }

    return (
        <div>
            <NewPost onClick={addPost} />
            <Posts posts={state.posts}/>
            <Paginator />
        </div>
    )
}

const NewPost = (props) => {
    return (
        <div>
            <h1>NEW POST HOLDER</h1>
            <button onClick={props.onClick}>Add Post</button>
        </div>
    )
}

const Posts = (props) => {
    return (
        <div>
            <h1>POSTS HOLDER</h1>
            {props.posts.map((item, index) => (
                <div>{item}</div>
            ))}
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
