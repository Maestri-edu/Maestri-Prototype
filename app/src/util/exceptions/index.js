export class InvalidRegexError extends Error {
    constructor(regex) {
        super(` the ${regex} is a unsafe Regex to use`);
        this.name = "InvalidRegexError"
    }
}