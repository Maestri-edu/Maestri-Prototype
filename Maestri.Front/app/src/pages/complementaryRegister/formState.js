

class FormComplementionRegisterState {
    #formInputsFields = {};

    setValues({...inputs}){
        console.log(inputs);
    }

    getValues(){
        return this.#formInputsFields;
    }
}

const formComplementionRegisterState = new FormComplementionRegisterState();

export default formComplementionRegisterState