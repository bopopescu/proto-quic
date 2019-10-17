// Copyright 2016 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// This file was generated by:
//   ./tools/json_schema_compiler/compiler.py.

/** @fileoverview Interface for languageSettingsPrivate that can be overriden. */

assertNotReached('Interface file for Closure Compiler should not be executed.');

/** @interface */
function LanguageSettingsPrivate() {}

LanguageSettingsPrivate.prototype = {
  /**
   * Gets languages available for translate, spell checking, input and locale.
   * @param {function(!Array<!chrome.languageSettingsPrivate.Language>):void}
   *     callback
   * @see https://developer.chrome.com/extensions/languageSettingsPrivate#method-getLanguageList
   */
  getLanguageList: assertNotReached,

  /**
   * Enables a language, adding it to the Accept-Language list (used to decide
   * which languages to translate, generate the Accept-Language header, etc.).
   * @param {string} languageCode
   * @see https://developer.chrome.com/extensions/languageSettingsPrivate#method-enableLanguage
   */
  enableLanguage: assertNotReached,

  /**
   * Disables a language, removing it from the Accept-Language list.
   * @param {string} languageCode
   * @see https://developer.chrome.com/extensions/languageSettingsPrivate#method-disableLanguage
   */
  disableLanguage: assertNotReached,

  /**
   * Gets the current status of the chosen spell check dictionaries.
   * @param {function(!Array<!chrome.languageSettingsPrivate.SpellcheckDictionaryStatus>):void}
   *     callback
   * @see https://developer.chrome.com/extensions/languageSettingsPrivate#method-getSpellcheckDictionaryStatuses
   */
  getSpellcheckDictionaryStatuses: assertNotReached,

  /**
   * Gets the custom spell check words, in sorted order.
   * @param {function(!Array<string>):void} callback
   * @see https://developer.chrome.com/extensions/languageSettingsPrivate#method-getSpellcheckWords
   */
  getSpellcheckWords: assertNotReached,

  /**
   * Adds a word to the custom dictionary.
   * @param {string} word
   * @see https://developer.chrome.com/extensions/languageSettingsPrivate#method-addSpellcheckWord
   */
  addSpellcheckWord: assertNotReached,

  /**
   * Removes a word from the custom dictionary.
   * @param {string} word
   * @see https://developer.chrome.com/extensions/languageSettingsPrivate#method-removeSpellcheckWord
   */
  removeSpellcheckWord: assertNotReached,

  /**
   * Gets the translate target language (in most cases, the display locale).
   * @param {function(string):void} callback
   * @see https://developer.chrome.com/extensions/languageSettingsPrivate#method-getTranslateTargetLanguage
   */
  getTranslateTargetLanguage: assertNotReached,

  /**
   * Gets all supported input methods, including third-party IMEs. Chrome OS
   * only.
   * @param {function(!chrome.languageSettingsPrivate.InputMethodLists):void}
   *     callback
   * @see https://developer.chrome.com/extensions/languageSettingsPrivate#method-getInputMethodLists
   */
  getInputMethodLists: assertNotReached,

  /**
   * Adds the input method to the current user's list of enabled input methods,
   * enabling the input method for the current user. Chrome OS only.
   * @param {string} inputMethodId
   * @see https://developer.chrome.com/extensions/languageSettingsPrivate#method-addInputMethod
   */
  addInputMethod: assertNotReached,

  /**
   * Removes the input method from the current user's list of enabled input
   * methods, disabling the input method for the current user. Chrome OS only.
   * @param {string} inputMethodId
   * @see https://developer.chrome.com/extensions/languageSettingsPrivate#method-removeInputMethod
   */
  removeInputMethod: assertNotReached,
};

/**
 * Called when the pref for the dictionaries used for spell checking changes or
 * the status of one of the spell check dictionaries changes.
 * @type {!ChromeEvent}
 * @see https://developer.chrome.com/extensions/languageSettingsPrivate#event-onSpellcheckDictionariesChanged
 */
LanguageSettingsPrivate.prototype.onSpellcheckDictionariesChanged;

/**
 * Called when words are added to and/or removed from the custom spell check
 * dictionary.
 * @type {!ChromeEvent}
 * @see https://developer.chrome.com/extensions/languageSettingsPrivate#event-onCustomDictionaryChanged
 */
LanguageSettingsPrivate.prototype.onCustomDictionaryChanged;

/**
 * Called when an input method is added.
 * @type {!ChromeEvent}
 * @see https://developer.chrome.com/extensions/languageSettingsPrivate#event-onInputMethodAdded
 */
LanguageSettingsPrivate.prototype.onInputMethodAdded;

/**
 * Called when an input method is removed.
 * @type {!ChromeEvent}
 * @see https://developer.chrome.com/extensions/languageSettingsPrivate#event-onInputMethodRemoved
 */
LanguageSettingsPrivate.prototype.onInputMethodRemoved;
