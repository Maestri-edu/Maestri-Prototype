

class FormComplementionRegisterState {
    #formInputsFields = {};

    addValues(inputs){
        Object.keys(inputs).forEach(key =>{
            this.#formInputsFields[key] = inputs[key];
        })
    }

    getValues(){
        return this.#formInputsFields;
    }
}

const formComplementionRegisterState = new FormComplementionRegisterState();

export default formComplementionRegisterState