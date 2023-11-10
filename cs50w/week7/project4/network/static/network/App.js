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
            <div>NEW POST HOLDER</div>
            <div>Value = {}</div>
        </div>
    )
}

const Posts = () => {
    return (
        <div>POSTS HOLDER</div>
    )
}

const Paginator = () => {
    return (
        <div>PAGINATOR HOLDER</div>
    )
}

ReactDOM.render(<App />, document.getElementById('App'))
