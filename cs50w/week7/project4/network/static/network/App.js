const App = () => {

    return (
        <div>
            <NewPost />
            <Posts />
            <Paginator />
        </div>
    )
}

const NewPost = () => {
    const [state, setState] = React.useSate({
        value: 0
    })
    return (
        <div>
            <h1>NEW POST HOLDER</h1>
            <div>Value = {state.value}</div>
        </div>
    )
}

const Posts = () => {
    return (
        <h1>POSTS HOLDER</h1>
    )
}

const Paginator = () => {
    return (
        <div>PAGINATOR HOLDER</div>
    )
}

ReactDOM.render(<App />, document.getElementById('App'))
