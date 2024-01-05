import safeRegex from "safe-regex";
import { InvalidRegexError } from "../exceptions";

export function isSafeRegex(regex) {
    if (safeRegex(regex)) {
        return true
    }
    throw new InvalidRegexError(regex);
}