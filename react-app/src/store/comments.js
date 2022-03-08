const LOAD = '/comments/LOAD';
const ADD = '/comments/ADD';
const DELETE = '/comments/DELETE';
const EDIT = '/comments/EDIT';

const load = (comments) => ({
    type: LOAD,
    comments
});

const add = (comment) => ({
    type: ADD,
    comment
});

const remove = (commentId) => ({
    type: DELETE,
    commentId
});

const edit = (comment) => ({
    type: EDIT,
    comment
});

export const getComment = (cheatsheetId) => async (dispatch) => {
    const response = await fetch(`/api/cheatsheets/${cheatsheetId}/comments`);
    if (response.ok) {
        const comments = await response.json();
        dispatch(load(comments));
        return comments;
    }
};

export const addComment = (payload) => async (dispatch) => {
    const response = await fetch(`/api/comments/new_comment`, {
        method: 'POST',
        header: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    })


    if (response.ok) {
        const newComment = await response.json();
        dispatch(add(newComment));
        return newComment;
    }
    return response
}

export const deleteComment = (payload) => async (dispatch) => {
    const response = await fetch(`/api/${payload.cheatsheetId}/comments/${payload.commentId}`, {
        method: 'DELETE'
    })

    if (response.ok) {
        dispatch(remove(payload.commentId));
        return;
    }
}


export const editComment = (payload) => async (dispatch) => {
    const response = await fetch(`/api/comments/${payload.commentId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    })

    if (response.ok) {
        const newComment = await response.json();
        dispatch(edit(newComment));
        return newComment;
    }
}


const initialState = {};

const commentReducer = (state = initialState, action) => {
    let newState;
    switch (action.type) {
        case LOAD:
            newState = {...state};
            action.cheatsheets['all_cheatsheets'].forEach(cheatsheet => newState[cheatsheet.id] = cheatsheet);
            return newState;
        case ADD:
            newState = { ...state };
            newState[action.comment.id] = action.comment;
            return newState;
        case DELETE:
            newState = { ...state };
            delete newState[action.commentId];
            return newState;
        case EDIT:
            newState = { ...state };
            newState[action.commment.id] = action.comment;
            return newState;
        default:
            return state
    }
}

export default commentReducer;
