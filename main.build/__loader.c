
/* Code to register embedded modules for meta path based loading if any. */

#include <Python.h>

#include "nuitka/constants_blob.h"

#include "nuitka/unfreezing.h"

/* Type bool */
#ifndef __cplusplus
#include "stdbool.h"
#endif

#if 772 > 0
static unsigned char *bytecode_data[772];
#else
static unsigned char **bytecode_data = NULL;
#endif

/* Table for lookup to find compiled or bytecode modules included in this
 * binary or module, or put along this binary as extension modules. We do
 * our own loading for each of these.
 */
extern PyObject *modulecode_PIL(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$BmpImagePlugin(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$GifImagePlugin(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$GimpGradientFile(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$GimpPaletteFile(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$Image(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$ImageChops(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$ImageColor(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$ImageFile(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$ImageFilter(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$ImageMode(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$ImageOps(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$ImagePalette(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$ImageQt(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$ImageSequence(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$ImageShow(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$JpegImagePlugin(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$JpegPresets(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$MpoImagePlugin(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$PaletteFile(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$PngImagePlugin(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$PpmImagePlugin(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$PyAccess(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$TiffImagePlugin(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$TiffTags(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$_binary(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$_util(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_PIL$_version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode___main__(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode__black_version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode__distutils_hack(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode__distutils_hack$override(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_asttokens(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_asttokens$asttokens(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_asttokens$line_numbers(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_asttokens$mark_tokens(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_asttokens$util(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_attr(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_attr$_cmp(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_attr$_compat(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_attr$_config(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_attr$_funcs(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_attr$_make(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_attr$_next_gen(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_attr$_version_info(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_attr$converters(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_attr$exceptions(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_attr$filters(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_attr$setters(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_attr$validators(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_backcall(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_backcall$_signatures(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_backcall$backcall(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_black(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_black$brackets(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_black$cache(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_black$comments(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_black$concurrency(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_black$const(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_black$files(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_black$handle_ipynb_magics(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_black$linegen(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_black$lines(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_black$mode(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_black$nodes(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_black$numerics(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_black$output(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_black$parsing(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_black$report(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_black$rusty(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_black$strings(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_black$trans(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_blib2to3(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_blib2to3$pgen2(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_blib2to3$pgen2$driver(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_blib2to3$pgen2$grammar(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_blib2to3$pgen2$parse(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_blib2to3$pgen2$pgen(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_blib2to3$pgen2$token(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_blib2to3$pgen2$tokenize(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_blib2to3$pygram(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_blib2to3$pytree(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_certifi(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_certifi$core(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cffi(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cffi$api(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cffi$cffi_opcode(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cffi$commontypes(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cffi$cparser(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cffi$error(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cffi$ffiplatform(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cffi$lock(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cffi$model(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cffi$pkgconfig(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cffi$recompiler(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cffi$vengine_cpy(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cffi$vengine_gen(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cffi$verifier(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_charset_normalizer(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_charset_normalizer$api(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_charset_normalizer$assets(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_charset_normalizer$cd(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_charset_normalizer$constant(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_charset_normalizer$legacy(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_charset_normalizer$md(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_charset_normalizer$models(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_charset_normalizer$utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_charset_normalizer$version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_click(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_click$_compat(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_click$_termui_impl(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_click$_textwrap(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_click$_unicodefun(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_click$_winconsole(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_click$core(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_click$decorators(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_click$exceptions(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_click$formatting(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_click$globals(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_click$parser(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_click$shell_completion(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_click$termui(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_click$types(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_click$utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_colorama(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_colorama$ansi(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_colorama$ansitowin32(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_colorama$initialise(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_colorama$win32(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_colorama$winterm(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_dateutil(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_dateutil$_common(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_dateutil$_version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_dateutil$easter(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_dateutil$parser(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_dateutil$parser$_parser(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_dateutil$parser$isoparser(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_dateutil$relativedelta(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_dateutil$rrule(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_dateutil$tz(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_dateutil$tz$_common(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_dateutil$tz$_factories(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_dateutil$tz$tz(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_dateutil$tz$win(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_dateutil$zoneinfo(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_debugpy(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_debugpy$_vendored(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_debugpy$_vendored$_util(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_debugpy$_vendored$force_pydevd(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_debugpy$_version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_debugpy$adapter(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_debugpy$common(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_debugpy$common$compat(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_debugpy$common$fmt(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_debugpy$common$json(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_debugpy$common$log(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_debugpy$common$sockets(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_debugpy$common$timestamp(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_debugpy$common$util(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_debugpy$server(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_debugpy$server$api(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_decorator(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_defusedxml(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_defusedxml$ElementTree(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_defusedxml$cElementTree(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_defusedxml$common(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_defusedxml$expatbuilder(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_defusedxml$expatreader(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_defusedxml$minidom(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_defusedxml$pulldom(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_defusedxml$sax(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_defusedxml$xmlrpc(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_entrypoints(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_executing(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_executing$executing(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_executing$version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_glcontext(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_glrenderer(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_idna(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_idna$core(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_idna$idnadata(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_idna$intranges(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_idna$package_data(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_idna$uts46data(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipykernel(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipykernel$_eventloop_macos(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipykernel$_version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipykernel$comm(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipykernel$comm$comm(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipykernel$comm$manager(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipykernel$compiler(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipykernel$connect(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipykernel$control(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipykernel$debugger(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipykernel$displayhook(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipykernel$embed(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipykernel$eventloops(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipykernel$gui(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipykernel$gui$gtk3embed(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipykernel$gui$gtkembed(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipykernel$heartbeat(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipykernel$iostream(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipykernel$ipkernel(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipykernel$jsonutil(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipykernel$kernelapp(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipykernel$kernelbase(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipykernel$kernelspec(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipykernel$parentpoller(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipykernel$pickleutil(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipykernel$serialize(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipykernel$trio_runner(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipykernel$zmqshell(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipython_genutils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipython_genutils$_version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipython_genutils$encoding(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipython_genutils$importstring(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipython_genutils$ipstruct(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ipython_genutils$py3compat(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$_compatibility(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$api(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$api$classes(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$api$completion(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$api$completion_cache(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$api$environment(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$api$errors(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$api$exceptions(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$api$file_name(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$api$helpers(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$api$interpreter(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$api$keywords(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$api$project(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$api$refactoring(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$api$refactoring$extract(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$api$strings(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$cache(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$common(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$debug(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$file_io(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$analysis(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$arguments(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$base_value(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$cache(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$compiled(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$compiled$access(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$compiled$getattr_static(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$compiled$mixed(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$compiled$subprocess(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$compiled$subprocess$functions(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$compiled$value(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$context(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$docstring_utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$docstrings(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$dynamic_params(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$filters(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$finder(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$flow_analysis(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$gradual(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$gradual$annotation(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$gradual$base(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$gradual$conversion(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$gradual$generics(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$gradual$stub_value(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$gradual$type_var(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$gradual$typeshed(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$gradual$typing(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$gradual$utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$helpers(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$imports(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$lazy_value(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$names(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$param(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$parser_cache(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$recursion(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$references(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$signature(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$star_args(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$syntax_tree(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$sys_path(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$value(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$value$decorator(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$value$dynamic_arrays(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$value$function(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$value$instance(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$value$iterable(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$value$klass(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$value$module(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$inference$value$namespace(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$parser_utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$plugins(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$plugins$django(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$plugins$flask(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$plugins$pytest(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$plugins$registry(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$plugins$stdlib(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jedi$settings(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jsonschema(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jsonschema$_format(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jsonschema$_legacy_validators(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jsonschema$_types(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jsonschema$_utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jsonschema$_validators(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jsonschema$exceptions(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jsonschema$protocols(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jsonschema$validators(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client$_version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client$adapter(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client$asynchronous(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client$asynchronous$client(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client$blocking(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client$blocking$client(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client$channels(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client$channelsabc(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client$client(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client$clientabc(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client$connect(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client$jsonutil(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client$kernelspec(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client$launcher(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client$localinterfaces(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client$manager(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client$managerabc(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client$multikernelmanager(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client$provisioning(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client$provisioning$factory(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client$provisioning$local_provisioner(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client$provisioning$provisioner_base(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client$session(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client$ssh(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client$ssh$forward(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client$ssh$tunnel(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client$utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_client$win_interrupt(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_core(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_core$paths(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_jupyter_core$version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_matplotlib_inline(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_matplotlib_inline$backend_inline(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_matplotlib_inline$config(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_moderngl(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_moderngl$buffer(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_moderngl$compute_shader(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_moderngl$conditional_render(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_moderngl$context(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_moderngl$error(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_moderngl$framebuffer(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_moderngl$program(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_moderngl$program_members(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_moderngl$program_members$attribute(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_moderngl$program_members$subroutine(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_moderngl$program_members$uniform(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_moderngl$program_members$uniform_block(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_moderngl$program_members$varying(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_moderngl$query(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_moderngl$renderbuffer(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_moderngl$sampler(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_moderngl$scope(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_moderngl$texture(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_moderngl$texture_3d(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_moderngl$texture_array(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_moderngl$texture_cube(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_moderngl$vertex_array(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_mypy_extensions(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$_compat(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$_version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$converter(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$corpus(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$corpus$words(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$json_compat(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$notebooknode(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$reader(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$sentinel(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$v1(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$v1$convert(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$v1$nbbase(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$v1$nbjson(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$v1$rwbase(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$v2(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$v2$convert(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$v2$nbbase(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$v2$nbjson(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$v2$nbpy(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$v2$nbxml(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$v2$rwbase(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$v3(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$v3$convert(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$v3$nbbase(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$v3$nbjson(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$v3$nbpy(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$v3$rwbase(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$v4(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$v4$convert(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$v4$nbbase(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$v4$nbjson(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$v4$rwbase(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nbformat$validator(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_nest_asyncio(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ntsecuritycon(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_packaging(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_packaging$__about__(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_parso(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_parso$_compatibility(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_parso$cache(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_parso$file_io(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_parso$grammar(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_parso$normalizer(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_parso$parser(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_parso$pgen2(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_parso$pgen2$generator(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_parso$pgen2$grammar_parser(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_parso$python(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_parso$python$diff(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_parso$python$errors(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_parso$python$parser(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_parso$python$pep8(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_parso$python$prefix(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_parso$python$token(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_parso$python$tokenize(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_parso$python$tree(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_parso$tree(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_parso$utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pathspec(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pathspec$_meta(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pathspec$compat(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pathspec$pathspec(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pathspec$pattern(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pathspec$patterns(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pathspec$patterns$gitwildmatch(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pathspec$util(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pickleshare(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_platformdirs(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_platformdirs$api(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_platformdirs$version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$application(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$application$application(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$application$current(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$application$dummy(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$application$run_in_terminal(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$auto_suggest(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$buffer(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$cache(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$clipboard(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$clipboard$base(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$clipboard$in_memory(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$completion(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$completion$base(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$completion$deduplicate(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$completion$filesystem(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$completion$fuzzy_completer(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$completion$nested(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$completion$word_completer(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$data_structures(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$document(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$enums(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$eventloop(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$eventloop$async_context_manager(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$eventloop$async_generator(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$eventloop$dummy_contextvars(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$eventloop$inputhook(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$eventloop$utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$eventloop$win32(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$filters(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$filters$app(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$filters$base(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$filters$cli(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$filters$utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$formatted_text(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$formatted_text$ansi(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$formatted_text$base(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$formatted_text$html(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$formatted_text$pygments(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$formatted_text$utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$history(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$input(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$input$ansi_escape_sequences(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$input$base(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$input$defaults(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$input$posix_pipe(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$input$posix_utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$input$typeahead(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$input$vt100(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$input$vt100_parser(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$input$win32(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$input$win32_pipe(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$key_binding(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$key_binding$bindings(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$key_binding$bindings$auto_suggest(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$key_binding$bindings$basic(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$key_binding$bindings$completion(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$key_binding$bindings$cpr(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$key_binding$bindings$emacs(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$key_binding$bindings$focus(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$key_binding$bindings$mouse(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$key_binding$bindings$named_commands(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$key_binding$bindings$open_in_editor(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$key_binding$bindings$page_navigation(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$key_binding$bindings$scroll(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$key_binding$bindings$search(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$key_binding$bindings$vi(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$key_binding$defaults(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$key_binding$digraphs(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$key_binding$emacs_state(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$key_binding$key_bindings(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$key_binding$key_processor(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$key_binding$vi_state(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$keys(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$layout(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$layout$containers(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$layout$controls(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$layout$dimension(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$layout$dummy(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$layout$layout(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$layout$margins(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$layout$menus(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$layout$mouse_handlers(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$layout$processors(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$layout$screen(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$layout$scrollable_pane(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$layout$utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$lexers(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$lexers$base(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$lexers$pygments(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$mouse_events(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$output(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$output$base(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$output$color_depth(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$output$conemu(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$output$defaults(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$output$vt100(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$output$win32(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$output$windows10(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$patch_stdout(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$renderer(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$search(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$selection(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$shortcuts(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$shortcuts$dialogs(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$shortcuts$progress_bar(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$shortcuts$progress_bar$base(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$shortcuts$progress_bar$formatters(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$shortcuts$prompt(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$shortcuts$utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$styles(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$styles$base(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$styles$defaults(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$styles$named_colors(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$styles$pygments(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$styles$style(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$styles$style_transformation(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$validation(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$widgets(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$widgets$base(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$widgets$dialogs(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$widgets$menus(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$widgets$toolbars(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_prompt_toolkit$win32_types(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pure_eval(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pure_eval$core(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pure_eval$my_getattr_static(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pure_eval$utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pure_eval$version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$colordict(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$compat(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$cursors(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$ftfont(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$locals(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$macosx(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$pkgdata(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$sndarray(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$sprite(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$surfarray(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$sysfont(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$threads(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygments(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygments$console(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygments$filter(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygments$filters(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygments$formatter(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygments$formatters(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygments$formatters$_mapping(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygments$formatters$terminal256(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygments$lexer(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygments$lexers(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygments$lexers$_mapping(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygments$modeline(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygments$plugin(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygments$regexopt(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygments$style(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygments$styles(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygments$token(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygments$util(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyrsistent(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyrsistent$_checked_types(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyrsistent$_field_common(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyrsistent$_helpers(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyrsistent$_immutable(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyrsistent$_pbag(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyrsistent$_pclass(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyrsistent$_pdeque(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyrsistent$_plist(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyrsistent$_pmap(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyrsistent$_precord(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyrsistent$_pset(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyrsistent$_pvector(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyrsistent$_toolz(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyrsistent$_transformations(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pythoncom(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pywin32_bootstrap(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pywin32_system32(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pywintypes(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_quadtree(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$__version__(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$_internal_utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$adapters(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$api(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$auth(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$certs(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$compat(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$cookies(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$exceptions(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$hooks(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$models(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$packages(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$sessions(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$status_codes(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$structures(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_six(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_stack_data(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_stack_data$core(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_stack_data$formatting(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_stack_data$utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_stack_data$version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_tomli(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_tomli$_parser(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_tomli$_re(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_tomli$_types(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_tornado(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_tornado$concurrent(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_tornado$escape(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_tornado$gen(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_tornado$ioloop(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_tornado$iostream(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_tornado$locks(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_tornado$log(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_tornado$netutil(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_tornado$options(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_tornado$platform(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_tornado$platform$asyncio(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_tornado$process(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_tornado$queues(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_tornado$util(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_traitlets(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_traitlets$_version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_traitlets$config(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_traitlets$config$application(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_traitlets$config$configurable(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_traitlets$config$loader(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_traitlets$log(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_traitlets$traitlets(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_traitlets$utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_traitlets$utils$bunch(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_traitlets$utils$decorators(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_traitlets$utils$descriptions(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_traitlets$utils$getargspec(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_traitlets$utils$importstring(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_traitlets$utils$sentinel(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_traitlets$utils$text(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_typing_extensions(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$_collections(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$_version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$connection(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$connectionpool(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$contrib(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$contrib$_appengine_environ(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$contrib$appengine(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$contrib$pyopenssl(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$contrib$socks(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$exceptions(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$fields(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$filepost(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$packages(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$packages$backports(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$packages$backports$makefile(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$packages$six(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$poolmanager(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$request(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$response(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$util(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$util$connection(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$util$proxy(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$util$queue(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$util$request(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$util$response(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$util$retry(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$util$ssl_(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$util$ssl_match_hostname(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$util$ssltransport(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$util$timeout(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$util$url(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$util$wait(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_wcwidth(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_wcwidth$table_wide(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_wcwidth$table_zero(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_wcwidth$unicode_versions(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_wcwidth$wcwidth(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_win32com(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_win32com$shell(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_win32com$shell$shellcon(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$_future(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$asyncio(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$backend(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$backend$cython(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$backend$select(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$error(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$eventloop(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$eventloop$_deprecated(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$eventloop$ioloop(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$eventloop$minitornado(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$eventloop$minitornado$concurrent(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$eventloop$minitornado$ioloop(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$eventloop$minitornado$log(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$eventloop$minitornado$platform(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$eventloop$minitornado$platform$auto(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$eventloop$minitornado$platform$common(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$eventloop$minitornado$platform$interface(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$eventloop$minitornado$platform$posix(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$eventloop$minitornado$platform$windows(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$eventloop$minitornado$stack_context(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$eventloop$minitornado$util(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$eventloop$zmqstream(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$sugar(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$sugar$attrsettr(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$sugar$constants(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$sugar$context(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$sugar$frame(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$sugar$poll(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$sugar$socket(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$sugar$stopwatch(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$sugar$tracker(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$sugar$version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$utils$constant_names(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$utils$interop(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$utils$jsonapi(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_zmq$utils$strtypes(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);

static struct Nuitka_MetaPathBasedLoaderEntry meta_path_loader_entries[] = {
    {"IPython", NULL, 0, 4838, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"IPython.core", NULL, 1, 176, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"IPython.core.alias", NULL, 2, 6995, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.application", NULL, 3, 14212, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.async_helpers", NULL, 4, 4953, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.autocall", NULL, 5, 2093, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.builtin_trap", NULL, 6, 2878, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.compilerop", NULL, 7, 4852, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.completer", NULL, 8, 64502, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.completerlib", NULL, 9, 9276, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.crashhandler", NULL, 10, 6659, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.debugger", NULL, 11, 25681, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.display", NULL, 12, 38791, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.display_functions", NULL, 13, 11895, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.display_trap", NULL, 14, 1744, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.displayhook", NULL, 15, 9507, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.displaypub", NULL, 16, 5087, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.error", NULL, 17, 1692, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.events", NULL, 18, 5587, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.excolors", NULL, 19, 2047, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.extensions", NULL, 20, 6370, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.formatters", NULL, 21, 30612, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.getipython", NULL, 22, 591, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.history", NULL, 23, 27992, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.hooks", NULL, 24, 5243, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.inputtransformer2", NULL, 25, 24182, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.interactiveshell", NULL, 26, 99820, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.latex_symbols", NULL, 27, 29422, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.logger", NULL, 28, 5326, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.macro", NULL, 29, 1785, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.magic", NULL, 30, 19685, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.magic_arguments", NULL, 31, 8625, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.magics", NULL, 32, 1403, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"IPython.core.magics.auto", NULL, 33, 3974, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.magics.basic", NULL, 34, 20496, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.magics.code", NULL, 35, 21386, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.magics.config", NULL, 36, 6723, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.magics.display", NULL, 37, 2999, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.magics.execution", NULL, 38, 44886, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.magics.extension", NULL, 39, 1956, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.magics.history", NULL, 40, 9428, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.magics.logging", NULL, 41, 5294, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.magics.namespace", NULL, 42, 20589, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.magics.osm", NULL, 43, 24710, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.magics.packaging", NULL, 44, 3025, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.magics.pylab", NULL, 45, 5668, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.magics.script", NULL, 46, 10018, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.oinspect", NULL, 47, 24994, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.page", NULL, 48, 8213, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.payload", NULL, 49, 1438, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.payloadpage", NULL, 50, 1438, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.prefilter", NULL, 51, 19960, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.profiledir", NULL, 52, 7524, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.pylabtools", NULL, 53, 9901, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.release", NULL, 54, 1159, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.shellapp", NULL, 55, 14147, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.splitinput", NULL, 56, 3594, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.ultratb", NULL, 57, 31607, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.core.usage", NULL, 58, 13285, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.display", NULL, 59, 900, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.extensions", NULL, 60, 241, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"IPython.extensions.storemagic", NULL, 61, 6785, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.external", NULL, 62, 357, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"IPython.external.qt_for_kernel", NULL, 63, 2581, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.external.qt_loaders", NULL, 64, 9511, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.lib", NULL, 65, 275, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"IPython.lib.clipboard", NULL, 66, 2401, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.lib.display", NULL, 67, 22532, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.lib.guisupport", NULL, 68, 5083, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.lib.pretty", NULL, 69, 27759, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.lib.security", NULL, 70, 2759, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.paths", NULL, 71, 3685, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.terminal", NULL, 72, 180, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"IPython.terminal.debugger", NULL, 73, 5377, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.terminal.embed", NULL, 74, 11825, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.terminal.interactiveshell", NULL, 75, 20670, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.terminal.ipapp", NULL, 76, 10143, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.terminal.magics", NULL, 77, 7599, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.terminal.prompts", NULL, 78, 4231, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.terminal.pt_inputhooks", NULL, 79, 1577, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"IPython.terminal.ptutils", NULL, 80, 5880, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.terminal.shortcuts", NULL, 81, 14487, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.testing", NULL, 82, 336, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"IPython.testing.skipdoctest", NULL, 83, 861, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils", NULL, 84, 177, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"IPython.utils.PyColorize", NULL, 85, 5979, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils._process_cli", NULL, 86, 1905, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils._process_common", NULL, 87, 5683, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils._process_posix", NULL, 88, 3941, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils._process_win32", NULL, 89, 5314, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils._sysinfo", NULL, 90, 197, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils.capture", NULL, 91, 5852, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils.colorable", NULL, 92, 987, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils.coloransi", NULL, 93, 6119, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils.contexts", NULL, 94, 1861, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils.data", NULL, 95, 1185, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils.decorators", NULL, 96, 1619, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils.dir2", NULL, 97, 2045, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils.encoding", NULL, 98, 1783, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils.frame", NULL, 99, 2901, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils.generics", NULL, 100, 1001, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils.importstring", NULL, 101, 1051, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils.io", NULL, 102, 4853, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils.ipstruct", NULL, 103, 10931, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils.module_paths", NULL, 104, 1334, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils.openpy", NULL, 105, 3481, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils.path", NULL, 106, 10643, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils.process", NULL, 107, 2093, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils.py3compat", NULL, 108, 1816, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils.sentinel", NULL, 109, 738, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils.strdispatch", NULL, 110, 2321, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils.sysinfo", NULL, 111, 3844, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils.syspathcontext", NULL, 112, 1855, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils.tempdir", NULL, 113, 2724, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils.terminal", NULL, 114, 3531, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils.text", NULL, 115, 22799, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils.timing", NULL, 116, 3561, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils.tokenutil", NULL, 117, 2704, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"IPython.utils.wildcard", NULL, 118, 3359, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"PIL", modulecode_PIL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"PIL.BmpImagePlugin", modulecode_PIL$BmpImagePlugin, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.GifImagePlugin", modulecode_PIL$GifImagePlugin, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.GimpGradientFile", modulecode_PIL$GimpGradientFile, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.GimpPaletteFile", modulecode_PIL$GimpPaletteFile, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.Image", modulecode_PIL$Image, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.ImageChops", modulecode_PIL$ImageChops, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.ImageColor", modulecode_PIL$ImageColor, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.ImageFile", modulecode_PIL$ImageFile, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.ImageFilter", modulecode_PIL$ImageFilter, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.ImageMode", modulecode_PIL$ImageMode, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.ImageOps", modulecode_PIL$ImageOps, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.ImagePalette", modulecode_PIL$ImagePalette, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.ImageQt", modulecode_PIL$ImageQt, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.ImageSequence", modulecode_PIL$ImageSequence, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.ImageShow", modulecode_PIL$ImageShow, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.JpegImagePlugin", modulecode_PIL$JpegImagePlugin, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.JpegPresets", modulecode_PIL$JpegPresets, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.MpoImagePlugin", modulecode_PIL$MpoImagePlugin, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.PaletteFile", modulecode_PIL$PaletteFile, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.PngImagePlugin", modulecode_PIL$PngImagePlugin, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.PpmImagePlugin", modulecode_PIL$PpmImagePlugin, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.PyAccess", modulecode_PIL$PyAccess, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.TiffImagePlugin", modulecode_PIL$TiffImagePlugin, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL.TiffTags", modulecode_PIL$TiffTags, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL._binary", modulecode_PIL$_binary, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL._imaging", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"PIL._util", modulecode_PIL$_util, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"PIL._version", modulecode_PIL$_version, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"__main__", modulecode___main__, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"_asyncio", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"_black_version", modulecode__black_version, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"_bz2", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"_cffi_backend", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"_ctypes", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"_decimal", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"_distutils_hack", modulecode__distutils_hack, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"_distutils_hack.override", modulecode__distutils_hack$override, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"_elementtree", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"_hashlib", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"_lzma", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"_msi", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"_multiprocessing", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"_overlapped", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"_queue", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"_socket", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"_sqlite3", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"_ssl", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"_tkinter", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"_uuid", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"_win32sysloader", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"_zoneinfo", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"asttokens", modulecode_asttokens, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"asttokens.asttokens", modulecode_asttokens$asttokens, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"asttokens.line_numbers", modulecode_asttokens$line_numbers, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"asttokens.mark_tokens", modulecode_asttokens$mark_tokens, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"asttokens.util", modulecode_asttokens$util, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"attr", modulecode_attr, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"attr._cmp", modulecode_attr$_cmp, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"attr._compat", modulecode_attr$_compat, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"attr._config", modulecode_attr$_config, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"attr._funcs", modulecode_attr$_funcs, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"attr._make", modulecode_attr$_make, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"attr._next_gen", modulecode_attr$_next_gen, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"attr._version_info", modulecode_attr$_version_info, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"attr.converters", modulecode_attr$converters, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"attr.exceptions", modulecode_attr$exceptions, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"attr.filters", modulecode_attr$filters, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"attr.setters", modulecode_attr$setters, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"attr.validators", modulecode_attr$validators, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"backcall", modulecode_backcall, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"backcall._signatures", modulecode_backcall$_signatures, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"backcall.backcall", modulecode_backcall$backcall, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"black", modulecode_black, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"black.brackets", modulecode_black$brackets, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"black.cache", modulecode_black$cache, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"black.comments", modulecode_black$comments, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"black.concurrency", modulecode_black$concurrency, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"black.const", modulecode_black$const, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"black.files", modulecode_black$files, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"black.handle_ipynb_magics", modulecode_black$handle_ipynb_magics, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"black.linegen", modulecode_black$linegen, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"black.lines", modulecode_black$lines, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"black.mode", modulecode_black$mode, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"black.nodes", modulecode_black$nodes, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"black.numerics", modulecode_black$numerics, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"black.output", modulecode_black$output, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"black.parsing", modulecode_black$parsing, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"black.report", modulecode_black$report, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"black.rusty", modulecode_black$rusty, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"black.strings", modulecode_black$strings, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"black.trans", modulecode_black$trans, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"blib2to3", modulecode_blib2to3, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"blib2to3.pgen2", modulecode_blib2to3$pgen2, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"blib2to3.pgen2.driver", modulecode_blib2to3$pgen2$driver, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"blib2to3.pgen2.grammar", modulecode_blib2to3$pgen2$grammar, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"blib2to3.pgen2.parse", modulecode_blib2to3$pgen2$parse, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"blib2to3.pgen2.pgen", modulecode_blib2to3$pgen2$pgen, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"blib2to3.pgen2.token", modulecode_blib2to3$pgen2$token, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"blib2to3.pgen2.tokenize", modulecode_blib2to3$pgen2$tokenize, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"blib2to3.pygram", modulecode_blib2to3$pygram, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"blib2to3.pytree", modulecode_blib2to3$pytree, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"certifi", modulecode_certifi, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"certifi.core", modulecode_certifi$core, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"cffi", modulecode_cffi, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"cffi.api", modulecode_cffi$api, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"cffi.cffi_opcode", modulecode_cffi$cffi_opcode, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"cffi.commontypes", modulecode_cffi$commontypes, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"cffi.cparser", modulecode_cffi$cparser, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"cffi.error", modulecode_cffi$error, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"cffi.ffiplatform", modulecode_cffi$ffiplatform, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"cffi.lock", modulecode_cffi$lock, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"cffi.model", modulecode_cffi$model, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"cffi.pkgconfig", modulecode_cffi$pkgconfig, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"cffi.recompiler", modulecode_cffi$recompiler, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"cffi.vengine_cpy", modulecode_cffi$vengine_cpy, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"cffi.vengine_gen", modulecode_cffi$vengine_gen, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"cffi.verifier", modulecode_cffi$verifier, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"charset_normalizer", modulecode_charset_normalizer, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"charset_normalizer.api", modulecode_charset_normalizer$api, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"charset_normalizer.assets", modulecode_charset_normalizer$assets, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"charset_normalizer.cd", modulecode_charset_normalizer$cd, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"charset_normalizer.constant", modulecode_charset_normalizer$constant, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"charset_normalizer.legacy", modulecode_charset_normalizer$legacy, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"charset_normalizer.md", modulecode_charset_normalizer$md, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"charset_normalizer.models", modulecode_charset_normalizer$models, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"charset_normalizer.utils", modulecode_charset_normalizer$utils, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"charset_normalizer.version", modulecode_charset_normalizer$version, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"click", modulecode_click, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"click._compat", modulecode_click$_compat, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"click._termui_impl", modulecode_click$_termui_impl, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"click._textwrap", modulecode_click$_textwrap, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"click._unicodefun", modulecode_click$_unicodefun, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"click._winconsole", modulecode_click$_winconsole, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"click.core", modulecode_click$core, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"click.decorators", modulecode_click$decorators, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"click.exceptions", modulecode_click$exceptions, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"click.formatting", modulecode_click$formatting, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"click.globals", modulecode_click$globals, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"click.parser", modulecode_click$parser, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"click.shell_completion", modulecode_click$shell_completion, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"click.termui", modulecode_click$termui, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"click.types", modulecode_click$types, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"click.utils", modulecode_click$utils, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"colorama", modulecode_colorama, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"colorama.ansi", modulecode_colorama$ansi, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"colorama.ansitowin32", modulecode_colorama$ansitowin32, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"colorama.initialise", modulecode_colorama$initialise, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"colorama.win32", modulecode_colorama$win32, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"colorama.winterm", modulecode_colorama$winterm, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"dateutil", modulecode_dateutil, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"dateutil._common", modulecode_dateutil$_common, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"dateutil._version", modulecode_dateutil$_version, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"dateutil.easter", modulecode_dateutil$easter, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"dateutil.parser", modulecode_dateutil$parser, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"dateutil.parser._parser", modulecode_dateutil$parser$_parser, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"dateutil.parser.isoparser", modulecode_dateutil$parser$isoparser, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"dateutil.relativedelta", modulecode_dateutil$relativedelta, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"dateutil.rrule", modulecode_dateutil$rrule, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"dateutil.tz", modulecode_dateutil$tz, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"dateutil.tz._common", modulecode_dateutil$tz$_common, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"dateutil.tz._factories", modulecode_dateutil$tz$_factories, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"dateutil.tz.tz", modulecode_dateutil$tz$tz, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"dateutil.tz.win", modulecode_dateutil$tz$win, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"dateutil.zoneinfo", modulecode_dateutil$zoneinfo, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"debugpy", modulecode_debugpy, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"debugpy._vendored", modulecode_debugpy$_vendored, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"debugpy._vendored._util", modulecode_debugpy$_vendored$_util, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"debugpy._vendored.force_pydevd", modulecode_debugpy$_vendored$force_pydevd, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"debugpy._version", modulecode_debugpy$_version, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"debugpy.adapter", modulecode_debugpy$adapter, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"debugpy.common", modulecode_debugpy$common, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"debugpy.common.compat", modulecode_debugpy$common$compat, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"debugpy.common.fmt", modulecode_debugpy$common$fmt, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"debugpy.common.json", modulecode_debugpy$common$json, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"debugpy.common.log", modulecode_debugpy$common$log, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"debugpy.common.sockets", modulecode_debugpy$common$sockets, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"debugpy.common.timestamp", modulecode_debugpy$common$timestamp, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"debugpy.common.util", modulecode_debugpy$common$util, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"debugpy.server", modulecode_debugpy$server, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"debugpy.server.api", modulecode_debugpy$server$api, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"decorator", modulecode_decorator, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"defusedxml", modulecode_defusedxml, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"defusedxml.ElementTree", modulecode_defusedxml$ElementTree, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"defusedxml.cElementTree", modulecode_defusedxml$cElementTree, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"defusedxml.common", modulecode_defusedxml$common, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"defusedxml.expatbuilder", modulecode_defusedxml$expatbuilder, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"defusedxml.expatreader", modulecode_defusedxml$expatreader, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"defusedxml.minidom", modulecode_defusedxml$minidom, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"defusedxml.pulldom", modulecode_defusedxml$pulldom, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"defusedxml.sax", modulecode_defusedxml$sax, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"defusedxml.xmlrpc", modulecode_defusedxml$xmlrpc, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"entrypoints", modulecode_entrypoints, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"executing", modulecode_executing, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"executing.executing", modulecode_executing$executing, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"executing.version", modulecode_executing$version, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"glcontext", modulecode_glcontext, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"glcontext.wgl", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"glrenderer", modulecode_glrenderer, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"idna", modulecode_idna, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"idna.core", modulecode_idna$core, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"idna.idnadata", modulecode_idna$idnadata, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"idna.intranges", modulecode_idna$intranges, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"idna.package_data", modulecode_idna$package_data, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"idna.uts46data", modulecode_idna$uts46data, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipykernel", modulecode_ipykernel, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"ipykernel._eventloop_macos", modulecode_ipykernel$_eventloop_macos, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipykernel._version", modulecode_ipykernel$_version, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipykernel.comm", modulecode_ipykernel$comm, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"ipykernel.comm.comm", modulecode_ipykernel$comm$comm, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipykernel.comm.manager", modulecode_ipykernel$comm$manager, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipykernel.compiler", modulecode_ipykernel$compiler, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipykernel.connect", modulecode_ipykernel$connect, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipykernel.control", modulecode_ipykernel$control, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipykernel.debugger", modulecode_ipykernel$debugger, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipykernel.displayhook", modulecode_ipykernel$displayhook, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipykernel.embed", modulecode_ipykernel$embed, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipykernel.eventloops", modulecode_ipykernel$eventloops, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipykernel.gui", modulecode_ipykernel$gui, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"ipykernel.gui.gtk3embed", modulecode_ipykernel$gui$gtk3embed, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipykernel.gui.gtkembed", modulecode_ipykernel$gui$gtkembed, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipykernel.heartbeat", modulecode_ipykernel$heartbeat, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipykernel.iostream", modulecode_ipykernel$iostream, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipykernel.ipkernel", modulecode_ipykernel$ipkernel, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipykernel.jsonutil", modulecode_ipykernel$jsonutil, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipykernel.kernelapp", modulecode_ipykernel$kernelapp, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipykernel.kernelbase", modulecode_ipykernel$kernelbase, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipykernel.kernelspec", modulecode_ipykernel$kernelspec, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipykernel.parentpoller", modulecode_ipykernel$parentpoller, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipykernel.pickleutil", modulecode_ipykernel$pickleutil, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipykernel.serialize", modulecode_ipykernel$serialize, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipykernel.trio_runner", modulecode_ipykernel$trio_runner, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipykernel.zmqshell", modulecode_ipykernel$zmqshell, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipython_genutils", modulecode_ipython_genutils, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"ipython_genutils._version", modulecode_ipython_genutils$_version, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipython_genutils.encoding", modulecode_ipython_genutils$encoding, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipython_genutils.importstring", modulecode_ipython_genutils$importstring, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipython_genutils.ipstruct", modulecode_ipython_genutils$ipstruct, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ipython_genutils.py3compat", modulecode_ipython_genutils$py3compat, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi", modulecode_jedi, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"jedi._compatibility", modulecode_jedi$_compatibility, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.api", modulecode_jedi$api, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"jedi.api.classes", modulecode_jedi$api$classes, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.api.completion", modulecode_jedi$api$completion, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.api.completion_cache", modulecode_jedi$api$completion_cache, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.api.environment", modulecode_jedi$api$environment, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.api.errors", modulecode_jedi$api$errors, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.api.exceptions", modulecode_jedi$api$exceptions, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.api.file_name", modulecode_jedi$api$file_name, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.api.helpers", modulecode_jedi$api$helpers, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.api.interpreter", modulecode_jedi$api$interpreter, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.api.keywords", modulecode_jedi$api$keywords, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.api.project", modulecode_jedi$api$project, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.api.refactoring", modulecode_jedi$api$refactoring, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"jedi.api.refactoring.extract", modulecode_jedi$api$refactoring$extract, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.api.strings", modulecode_jedi$api$strings, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.cache", modulecode_jedi$cache, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.common", modulecode_jedi$common, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.debug", modulecode_jedi$debug, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.file_io", modulecode_jedi$file_io, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference", modulecode_jedi$inference, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"jedi.inference.analysis", modulecode_jedi$inference$analysis, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.arguments", modulecode_jedi$inference$arguments, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.base_value", modulecode_jedi$inference$base_value, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.cache", modulecode_jedi$inference$cache, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.compiled", modulecode_jedi$inference$compiled, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"jedi.inference.compiled.access", modulecode_jedi$inference$compiled$access, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.compiled.getattr_static", modulecode_jedi$inference$compiled$getattr_static, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.compiled.mixed", modulecode_jedi$inference$compiled$mixed, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.compiled.subprocess", modulecode_jedi$inference$compiled$subprocess, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"jedi.inference.compiled.subprocess.functions", modulecode_jedi$inference$compiled$subprocess$functions, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.compiled.value", modulecode_jedi$inference$compiled$value, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.context", modulecode_jedi$inference$context, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.docstring_utils", modulecode_jedi$inference$docstring_utils, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.docstrings", modulecode_jedi$inference$docstrings, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.dynamic_params", modulecode_jedi$inference$dynamic_params, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.filters", modulecode_jedi$inference$filters, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.finder", modulecode_jedi$inference$finder, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.flow_analysis", modulecode_jedi$inference$flow_analysis, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.gradual", modulecode_jedi$inference$gradual, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"jedi.inference.gradual.annotation", modulecode_jedi$inference$gradual$annotation, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.gradual.base", modulecode_jedi$inference$gradual$base, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.gradual.conversion", modulecode_jedi$inference$gradual$conversion, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.gradual.generics", modulecode_jedi$inference$gradual$generics, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.gradual.stub_value", modulecode_jedi$inference$gradual$stub_value, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.gradual.type_var", modulecode_jedi$inference$gradual$type_var, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.gradual.typeshed", modulecode_jedi$inference$gradual$typeshed, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.gradual.typing", modulecode_jedi$inference$gradual$typing, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.gradual.utils", modulecode_jedi$inference$gradual$utils, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.helpers", modulecode_jedi$inference$helpers, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.imports", modulecode_jedi$inference$imports, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.lazy_value", modulecode_jedi$inference$lazy_value, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.names", modulecode_jedi$inference$names, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.param", modulecode_jedi$inference$param, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.parser_cache", modulecode_jedi$inference$parser_cache, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.recursion", modulecode_jedi$inference$recursion, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.references", modulecode_jedi$inference$references, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.signature", modulecode_jedi$inference$signature, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.star_args", modulecode_jedi$inference$star_args, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.syntax_tree", modulecode_jedi$inference$syntax_tree, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.sys_path", modulecode_jedi$inference$sys_path, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.utils", modulecode_jedi$inference$utils, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.value", modulecode_jedi$inference$value, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"jedi.inference.value.decorator", modulecode_jedi$inference$value$decorator, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.value.dynamic_arrays", modulecode_jedi$inference$value$dynamic_arrays, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.value.function", modulecode_jedi$inference$value$function, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.value.instance", modulecode_jedi$inference$value$instance, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.value.iterable", modulecode_jedi$inference$value$iterable, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.value.klass", modulecode_jedi$inference$value$klass, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.value.module", modulecode_jedi$inference$value$module, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.inference.value.namespace", modulecode_jedi$inference$value$namespace, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.parser_utils", modulecode_jedi$parser_utils, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.plugins", modulecode_jedi$plugins, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"jedi.plugins.django", modulecode_jedi$plugins$django, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.plugins.flask", modulecode_jedi$plugins$flask, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.plugins.pytest", modulecode_jedi$plugins$pytest, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.plugins.registry", modulecode_jedi$plugins$registry, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.plugins.stdlib", modulecode_jedi$plugins$stdlib, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jedi.settings", modulecode_jedi$settings, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jsonschema", modulecode_jsonschema, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"jsonschema._format", modulecode_jsonschema$_format, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jsonschema._legacy_validators", modulecode_jsonschema$_legacy_validators, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jsonschema._types", modulecode_jsonschema$_types, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jsonschema._utils", modulecode_jsonschema$_utils, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jsonschema._validators", modulecode_jsonschema$_validators, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jsonschema.exceptions", modulecode_jsonschema$exceptions, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jsonschema.protocols", modulecode_jsonschema$protocols, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jsonschema.validators", modulecode_jsonschema$validators, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jupyter_client", modulecode_jupyter_client, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"jupyter_client._version", modulecode_jupyter_client$_version, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jupyter_client.adapter", modulecode_jupyter_client$adapter, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jupyter_client.asynchronous", modulecode_jupyter_client$asynchronous, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"jupyter_client.asynchronous.client", modulecode_jupyter_client$asynchronous$client, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jupyter_client.blocking", modulecode_jupyter_client$blocking, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"jupyter_client.blocking.client", modulecode_jupyter_client$blocking$client, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jupyter_client.channels", modulecode_jupyter_client$channels, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jupyter_client.channelsabc", modulecode_jupyter_client$channelsabc, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jupyter_client.client", modulecode_jupyter_client$client, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jupyter_client.clientabc", modulecode_jupyter_client$clientabc, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jupyter_client.connect", modulecode_jupyter_client$connect, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jupyter_client.jsonutil", modulecode_jupyter_client$jsonutil, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jupyter_client.kernelspec", modulecode_jupyter_client$kernelspec, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jupyter_client.launcher", modulecode_jupyter_client$launcher, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jupyter_client.localinterfaces", modulecode_jupyter_client$localinterfaces, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jupyter_client.manager", modulecode_jupyter_client$manager, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jupyter_client.managerabc", modulecode_jupyter_client$managerabc, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jupyter_client.multikernelmanager", modulecode_jupyter_client$multikernelmanager, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jupyter_client.provisioning", modulecode_jupyter_client$provisioning, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"jupyter_client.provisioning.factory", modulecode_jupyter_client$provisioning$factory, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jupyter_client.provisioning.local_provisioner", modulecode_jupyter_client$provisioning$local_provisioner, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jupyter_client.provisioning.provisioner_base", modulecode_jupyter_client$provisioning$provisioner_base, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jupyter_client.session", modulecode_jupyter_client$session, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jupyter_client.ssh", modulecode_jupyter_client$ssh, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"jupyter_client.ssh.forward", modulecode_jupyter_client$ssh$forward, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jupyter_client.ssh.tunnel", modulecode_jupyter_client$ssh$tunnel, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jupyter_client.utils", modulecode_jupyter_client$utils, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jupyter_client.win_interrupt", modulecode_jupyter_client$win_interrupt, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jupyter_core", modulecode_jupyter_core, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"jupyter_core.paths", modulecode_jupyter_core$paths, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"jupyter_core.version", modulecode_jupyter_core$version, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"matplotlib_inline", modulecode_matplotlib_inline, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"matplotlib_inline.backend_inline", modulecode_matplotlib_inline$backend_inline, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"matplotlib_inline.config", modulecode_matplotlib_inline$config, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"moderngl", modulecode_moderngl, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"moderngl.buffer", modulecode_moderngl$buffer, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"moderngl.compute_shader", modulecode_moderngl$compute_shader, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"moderngl.conditional_render", modulecode_moderngl$conditional_render, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"moderngl.context", modulecode_moderngl$context, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"moderngl.error", modulecode_moderngl$error, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"moderngl.framebuffer", modulecode_moderngl$framebuffer, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"moderngl.mgl", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"moderngl.program", modulecode_moderngl$program, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"moderngl.program_members", modulecode_moderngl$program_members, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"moderngl.program_members.attribute", modulecode_moderngl$program_members$attribute, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"moderngl.program_members.subroutine", modulecode_moderngl$program_members$subroutine, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"moderngl.program_members.uniform", modulecode_moderngl$program_members$uniform, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"moderngl.program_members.uniform_block", modulecode_moderngl$program_members$uniform_block, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"moderngl.program_members.varying", modulecode_moderngl$program_members$varying, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"moderngl.query", modulecode_moderngl$query, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"moderngl.renderbuffer", modulecode_moderngl$renderbuffer, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"moderngl.sampler", modulecode_moderngl$sampler, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"moderngl.scope", modulecode_moderngl$scope, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"moderngl.texture", modulecode_moderngl$texture, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"moderngl.texture_3d", modulecode_moderngl$texture_3d, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"moderngl.texture_array", modulecode_moderngl$texture_array, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"moderngl.texture_cube", modulecode_moderngl$texture_cube, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"moderngl.vertex_array", modulecode_moderngl$vertex_array, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"mypy_extensions", modulecode_mypy_extensions, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nbformat", modulecode_nbformat, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"nbformat._compat", modulecode_nbformat$_compat, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nbformat._version", modulecode_nbformat$_version, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nbformat.converter", modulecode_nbformat$converter, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nbformat.corpus", modulecode_nbformat$corpus, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"nbformat.corpus.words", modulecode_nbformat$corpus$words, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nbformat.json_compat", modulecode_nbformat$json_compat, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nbformat.notebooknode", modulecode_nbformat$notebooknode, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nbformat.reader", modulecode_nbformat$reader, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nbformat.sentinel", modulecode_nbformat$sentinel, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nbformat.v1", modulecode_nbformat$v1, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"nbformat.v1.convert", modulecode_nbformat$v1$convert, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nbformat.v1.nbbase", modulecode_nbformat$v1$nbbase, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nbformat.v1.nbjson", modulecode_nbformat$v1$nbjson, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nbformat.v1.rwbase", modulecode_nbformat$v1$rwbase, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nbformat.v2", modulecode_nbformat$v2, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"nbformat.v2.convert", modulecode_nbformat$v2$convert, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nbformat.v2.nbbase", modulecode_nbformat$v2$nbbase, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nbformat.v2.nbjson", modulecode_nbformat$v2$nbjson, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nbformat.v2.nbpy", modulecode_nbformat$v2$nbpy, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nbformat.v2.nbxml", modulecode_nbformat$v2$nbxml, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nbformat.v2.rwbase", modulecode_nbformat$v2$rwbase, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nbformat.v3", modulecode_nbformat$v3, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"nbformat.v3.convert", modulecode_nbformat$v3$convert, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nbformat.v3.nbbase", modulecode_nbformat$v3$nbbase, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nbformat.v3.nbjson", modulecode_nbformat$v3$nbjson, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nbformat.v3.nbpy", modulecode_nbformat$v3$nbpy, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nbformat.v3.rwbase", modulecode_nbformat$v3$rwbase, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nbformat.v4", modulecode_nbformat$v4, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"nbformat.v4.convert", modulecode_nbformat$v4$convert, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nbformat.v4.nbbase", modulecode_nbformat$v4$nbbase, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nbformat.v4.nbjson", modulecode_nbformat$v4$nbjson, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nbformat.v4.rwbase", modulecode_nbformat$v4$rwbase, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nbformat.validator", modulecode_nbformat$validator, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"nest_asyncio", modulecode_nest_asyncio, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"ntsecuritycon", modulecode_ntsecuritycon, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"packaging", modulecode_packaging, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"packaging.__about__", modulecode_packaging$__about__, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"parso", modulecode_parso, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"parso._compatibility", modulecode_parso$_compatibility, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"parso.cache", modulecode_parso$cache, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"parso.file_io", modulecode_parso$file_io, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"parso.grammar", modulecode_parso$grammar, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"parso.normalizer", modulecode_parso$normalizer, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"parso.parser", modulecode_parso$parser, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"parso.pgen2", modulecode_parso$pgen2, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"parso.pgen2.generator", modulecode_parso$pgen2$generator, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"parso.pgen2.grammar_parser", modulecode_parso$pgen2$grammar_parser, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"parso.python", modulecode_parso$python, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"parso.python.diff", modulecode_parso$python$diff, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"parso.python.errors", modulecode_parso$python$errors, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"parso.python.parser", modulecode_parso$python$parser, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"parso.python.pep8", modulecode_parso$python$pep8, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"parso.python.prefix", modulecode_parso$python$prefix, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"parso.python.token", modulecode_parso$python$token, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"parso.python.tokenize", modulecode_parso$python$tokenize, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"parso.python.tree", modulecode_parso$python$tree, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"parso.tree", modulecode_parso$tree, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"parso.utils", modulecode_parso$utils, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pathspec", modulecode_pathspec, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"pathspec._meta", modulecode_pathspec$_meta, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pathspec.compat", modulecode_pathspec$compat, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pathspec.pathspec", modulecode_pathspec$pathspec, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pathspec.pattern", modulecode_pathspec$pattern, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pathspec.patterns", modulecode_pathspec$patterns, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"pathspec.patterns.gitwildmatch", modulecode_pathspec$patterns$gitwildmatch, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pathspec.util", modulecode_pathspec$util, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pickleshare", modulecode_pickleshare, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pkg_resources", NULL, 119, 100431, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"pkg_resources._vendor", NULL, 120, 185, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"pkg_resources._vendor.appdirs", NULL, 121, 20502, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pkg_resources._vendor.packaging", NULL, 122, 547, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"pkg_resources._vendor.packaging.__about__", NULL, 123, 701, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pkg_resources._vendor.packaging._compat", NULL, 124, 1145, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pkg_resources._vendor.packaging._structures", NULL, 125, 2899, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pkg_resources._vendor.packaging._typing", NULL, 126, 1490, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pkg_resources._vendor.packaging.markers", NULL, 127, 9306, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pkg_resources._vendor.packaging.requirements", NULL, 128, 4083, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pkg_resources._vendor.packaging.specifiers", NULL, 129, 20582, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pkg_resources._vendor.packaging.utils", NULL, 130, 1652, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pkg_resources._vendor.packaging.version", NULL, 131, 13319, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pkg_resources._vendor.pyparsing", NULL, 132, 201339, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pkg_resources.extern", NULL, 133, 2874, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"platformdirs", modulecode_platformdirs, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"platformdirs.api", modulecode_platformdirs$api, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"platformdirs.version", modulecode_platformdirs$version, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit", modulecode_prompt_toolkit, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"prompt_toolkit.application", modulecode_prompt_toolkit$application, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"prompt_toolkit.application.application", modulecode_prompt_toolkit$application$application, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.application.current", modulecode_prompt_toolkit$application$current, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.application.dummy", modulecode_prompt_toolkit$application$dummy, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.application.run_in_terminal", modulecode_prompt_toolkit$application$run_in_terminal, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.auto_suggest", modulecode_prompt_toolkit$auto_suggest, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.buffer", modulecode_prompt_toolkit$buffer, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.cache", modulecode_prompt_toolkit$cache, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.clipboard", modulecode_prompt_toolkit$clipboard, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"prompt_toolkit.clipboard.base", modulecode_prompt_toolkit$clipboard$base, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.clipboard.in_memory", modulecode_prompt_toolkit$clipboard$in_memory, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.completion", modulecode_prompt_toolkit$completion, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"prompt_toolkit.completion.base", modulecode_prompt_toolkit$completion$base, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.completion.deduplicate", modulecode_prompt_toolkit$completion$deduplicate, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.completion.filesystem", modulecode_prompt_toolkit$completion$filesystem, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.completion.fuzzy_completer", modulecode_prompt_toolkit$completion$fuzzy_completer, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.completion.nested", modulecode_prompt_toolkit$completion$nested, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.completion.word_completer", modulecode_prompt_toolkit$completion$word_completer, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.data_structures", modulecode_prompt_toolkit$data_structures, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.document", modulecode_prompt_toolkit$document, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.enums", modulecode_prompt_toolkit$enums, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.eventloop", modulecode_prompt_toolkit$eventloop, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"prompt_toolkit.eventloop.async_context_manager", modulecode_prompt_toolkit$eventloop$async_context_manager, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.eventloop.async_generator", modulecode_prompt_toolkit$eventloop$async_generator, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.eventloop.dummy_contextvars", modulecode_prompt_toolkit$eventloop$dummy_contextvars, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.eventloop.inputhook", modulecode_prompt_toolkit$eventloop$inputhook, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.eventloop.utils", modulecode_prompt_toolkit$eventloop$utils, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.eventloop.win32", modulecode_prompt_toolkit$eventloop$win32, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.filters", modulecode_prompt_toolkit$filters, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"prompt_toolkit.filters.app", modulecode_prompt_toolkit$filters$app, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.filters.base", modulecode_prompt_toolkit$filters$base, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.filters.cli", modulecode_prompt_toolkit$filters$cli, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.filters.utils", modulecode_prompt_toolkit$filters$utils, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.formatted_text", modulecode_prompt_toolkit$formatted_text, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"prompt_toolkit.formatted_text.ansi", modulecode_prompt_toolkit$formatted_text$ansi, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.formatted_text.base", modulecode_prompt_toolkit$formatted_text$base, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.formatted_text.html", modulecode_prompt_toolkit$formatted_text$html, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.formatted_text.pygments", modulecode_prompt_toolkit$formatted_text$pygments, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.formatted_text.utils", modulecode_prompt_toolkit$formatted_text$utils, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.history", modulecode_prompt_toolkit$history, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.input", modulecode_prompt_toolkit$input, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"prompt_toolkit.input.ansi_escape_sequences", modulecode_prompt_toolkit$input$ansi_escape_sequences, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.input.base", modulecode_prompt_toolkit$input$base, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.input.defaults", modulecode_prompt_toolkit$input$defaults, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.input.posix_pipe", modulecode_prompt_toolkit$input$posix_pipe, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.input.posix_utils", modulecode_prompt_toolkit$input$posix_utils, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.input.typeahead", modulecode_prompt_toolkit$input$typeahead, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.input.vt100", modulecode_prompt_toolkit$input$vt100, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.input.vt100_parser", modulecode_prompt_toolkit$input$vt100_parser, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.input.win32", modulecode_prompt_toolkit$input$win32, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.input.win32_pipe", modulecode_prompt_toolkit$input$win32_pipe, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.key_binding", modulecode_prompt_toolkit$key_binding, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"prompt_toolkit.key_binding.bindings", modulecode_prompt_toolkit$key_binding$bindings, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"prompt_toolkit.key_binding.bindings.auto_suggest", modulecode_prompt_toolkit$key_binding$bindings$auto_suggest, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.key_binding.bindings.basic", modulecode_prompt_toolkit$key_binding$bindings$basic, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.key_binding.bindings.completion", modulecode_prompt_toolkit$key_binding$bindings$completion, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.key_binding.bindings.cpr", modulecode_prompt_toolkit$key_binding$bindings$cpr, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.key_binding.bindings.emacs", modulecode_prompt_toolkit$key_binding$bindings$emacs, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.key_binding.bindings.focus", modulecode_prompt_toolkit$key_binding$bindings$focus, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.key_binding.bindings.mouse", modulecode_prompt_toolkit$key_binding$bindings$mouse, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.key_binding.bindings.named_commands", modulecode_prompt_toolkit$key_binding$bindings$named_commands, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.key_binding.bindings.open_in_editor", modulecode_prompt_toolkit$key_binding$bindings$open_in_editor, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.key_binding.bindings.page_navigation", modulecode_prompt_toolkit$key_binding$bindings$page_navigation, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.key_binding.bindings.scroll", modulecode_prompt_toolkit$key_binding$bindings$scroll, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.key_binding.bindings.search", modulecode_prompt_toolkit$key_binding$bindings$search, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.key_binding.bindings.vi", modulecode_prompt_toolkit$key_binding$bindings$vi, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.key_binding.defaults", modulecode_prompt_toolkit$key_binding$defaults, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.key_binding.digraphs", modulecode_prompt_toolkit$key_binding$digraphs, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.key_binding.emacs_state", modulecode_prompt_toolkit$key_binding$emacs_state, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.key_binding.key_bindings", modulecode_prompt_toolkit$key_binding$key_bindings, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.key_binding.key_processor", modulecode_prompt_toolkit$key_binding$key_processor, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.key_binding.vi_state", modulecode_prompt_toolkit$key_binding$vi_state, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.keys", modulecode_prompt_toolkit$keys, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.layout", modulecode_prompt_toolkit$layout, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"prompt_toolkit.layout.containers", modulecode_prompt_toolkit$layout$containers, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.layout.controls", modulecode_prompt_toolkit$layout$controls, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.layout.dimension", modulecode_prompt_toolkit$layout$dimension, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.layout.dummy", modulecode_prompt_toolkit$layout$dummy, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.layout.layout", modulecode_prompt_toolkit$layout$layout, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.layout.margins", modulecode_prompt_toolkit$layout$margins, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.layout.menus", modulecode_prompt_toolkit$layout$menus, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.layout.mouse_handlers", modulecode_prompt_toolkit$layout$mouse_handlers, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.layout.processors", modulecode_prompt_toolkit$layout$processors, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.layout.screen", modulecode_prompt_toolkit$layout$screen, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.layout.scrollable_pane", modulecode_prompt_toolkit$layout$scrollable_pane, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.layout.utils", modulecode_prompt_toolkit$layout$utils, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.lexers", modulecode_prompt_toolkit$lexers, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"prompt_toolkit.lexers.base", modulecode_prompt_toolkit$lexers$base, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.lexers.pygments", modulecode_prompt_toolkit$lexers$pygments, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.mouse_events", modulecode_prompt_toolkit$mouse_events, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.output", modulecode_prompt_toolkit$output, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"prompt_toolkit.output.base", modulecode_prompt_toolkit$output$base, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.output.color_depth", modulecode_prompt_toolkit$output$color_depth, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.output.conemu", modulecode_prompt_toolkit$output$conemu, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.output.defaults", modulecode_prompt_toolkit$output$defaults, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.output.vt100", modulecode_prompt_toolkit$output$vt100, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.output.win32", modulecode_prompt_toolkit$output$win32, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.output.windows10", modulecode_prompt_toolkit$output$windows10, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.patch_stdout", modulecode_prompt_toolkit$patch_stdout, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.renderer", modulecode_prompt_toolkit$renderer, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.search", modulecode_prompt_toolkit$search, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.selection", modulecode_prompt_toolkit$selection, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.shortcuts", modulecode_prompt_toolkit$shortcuts, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"prompt_toolkit.shortcuts.dialogs", modulecode_prompt_toolkit$shortcuts$dialogs, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.shortcuts.progress_bar", modulecode_prompt_toolkit$shortcuts$progress_bar, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"prompt_toolkit.shortcuts.progress_bar.base", modulecode_prompt_toolkit$shortcuts$progress_bar$base, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.shortcuts.progress_bar.formatters", modulecode_prompt_toolkit$shortcuts$progress_bar$formatters, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.shortcuts.prompt", modulecode_prompt_toolkit$shortcuts$prompt, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.shortcuts.utils", modulecode_prompt_toolkit$shortcuts$utils, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.styles", modulecode_prompt_toolkit$styles, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"prompt_toolkit.styles.base", modulecode_prompt_toolkit$styles$base, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.styles.defaults", modulecode_prompt_toolkit$styles$defaults, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.styles.named_colors", modulecode_prompt_toolkit$styles$named_colors, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.styles.pygments", modulecode_prompt_toolkit$styles$pygments, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.styles.style", modulecode_prompt_toolkit$styles$style, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.styles.style_transformation", modulecode_prompt_toolkit$styles$style_transformation, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.utils", modulecode_prompt_toolkit$utils, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.validation", modulecode_prompt_toolkit$validation, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.widgets", modulecode_prompt_toolkit$widgets, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"prompt_toolkit.widgets.base", modulecode_prompt_toolkit$widgets$base, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.widgets.dialogs", modulecode_prompt_toolkit$widgets$dialogs, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.widgets.menus", modulecode_prompt_toolkit$widgets$menus, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.widgets.toolbars", modulecode_prompt_toolkit$widgets$toolbars, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"prompt_toolkit.win32_types", modulecode_prompt_toolkit$win32_types, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pure_eval", modulecode_pure_eval, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"pure_eval.core", modulecode_pure_eval$core, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pure_eval.my_getattr_static", modulecode_pure_eval$my_getattr_static, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pure_eval.utils", modulecode_pure_eval$utils, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pure_eval.version", modulecode_pure_eval$version, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pvectorc", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pycparser", NULL, 134, 2516, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"pycparser.ast_transforms", NULL, 135, 3738, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pycparser.c_ast", NULL, 136, 36569, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pycparser.c_lexer", NULL, 137, 13104, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pycparser.c_parser", NULL, 138, 64585, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pycparser.lextab", NULL, 139, 6609, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pycparser.ply", NULL, 140, 226, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"pycparser.ply.lex", NULL, 141, 21420, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pycparser.ply.yacc", NULL, 142, 52975, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pycparser.plyparser", NULL, 143, 4677, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pycparser.yacctab", NULL, 144, 175820, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pyexpat", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame", modulecode_pygame, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"pygame._freetype", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame.base", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame.bufferproxy", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame.color", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame.colordict", modulecode_pygame$colordict, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygame.compat", modulecode_pygame$compat, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygame.constants", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame.cursors", modulecode_pygame$cursors, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygame.display", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame.draw", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame.event", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame.fastevent", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame.font", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame.ftfont", modulecode_pygame$ftfont, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygame.image", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame.imageext", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame.joystick", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame.key", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame.locals", modulecode_pygame$locals, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygame.macosx", modulecode_pygame$macosx, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygame.mask", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame.math", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame.mixer", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame.mixer_music", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame.mouse", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame.pixelarray", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame.pixelcopy", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame.pkgdata", modulecode_pygame$pkgdata, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygame.rect", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame.rwobject", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame.scrap", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame.sndarray", modulecode_pygame$sndarray, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygame.sprite", modulecode_pygame$sprite, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygame.surface", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame.surfarray", modulecode_pygame$surfarray, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygame.surflock", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame.sysfont", modulecode_pygame$sysfont, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygame.threads", modulecode_pygame$threads, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"pygame.time", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame.transform", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"pygame.version", modulecode_pygame$version, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygments", modulecode_pygments, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"pygments.console", modulecode_pygments$console, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygments.filter", modulecode_pygments$filter, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygments.filters", modulecode_pygments$filters, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"pygments.formatter", modulecode_pygments$formatter, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygments.formatters", modulecode_pygments$formatters, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"pygments.formatters._mapping", modulecode_pygments$formatters$_mapping, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygments.formatters.terminal256", modulecode_pygments$formatters$terminal256, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygments.lexer", modulecode_pygments$lexer, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygments.lexers", modulecode_pygments$lexers, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"pygments.lexers._mapping", modulecode_pygments$lexers$_mapping, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygments.modeline", modulecode_pygments$modeline, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygments.plugin", modulecode_pygments$plugin, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygments.regexopt", modulecode_pygments$regexopt, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygments.style", modulecode_pygments$style, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygments.styles", modulecode_pygments$styles, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"pygments.token", modulecode_pygments$token, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygments.util", modulecode_pygments$util, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyrsistent", modulecode_pyrsistent, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"pyrsistent._checked_types", modulecode_pyrsistent$_checked_types, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyrsistent._field_common", modulecode_pyrsistent$_field_common, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyrsistent._helpers", modulecode_pyrsistent$_helpers, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyrsistent._immutable", modulecode_pyrsistent$_immutable, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyrsistent._pbag", modulecode_pyrsistent$_pbag, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyrsistent._pclass", modulecode_pyrsistent$_pclass, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyrsistent._pdeque", modulecode_pyrsistent$_pdeque, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyrsistent._plist", modulecode_pyrsistent$_plist, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyrsistent._pmap", modulecode_pyrsistent$_pmap, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyrsistent._precord", modulecode_pyrsistent$_precord, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyrsistent._pset", modulecode_pyrsistent$_pset, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyrsistent._pvector", modulecode_pyrsistent$_pvector, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyrsistent._toolz", modulecode_pyrsistent$_toolz, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pyrsistent._transformations", modulecode_pyrsistent$_transformations, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pythoncom", modulecode_pythoncom, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pywin32_bootstrap", modulecode_pywin32_bootstrap, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pywin32_system32", modulecode_pywin32_system32, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"pywintypes", modulecode_pywintypes, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"quadtree", modulecode_quadtree, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"requests", modulecode_requests, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"requests.__version__", modulecode_requests$__version__, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"requests._internal_utils", modulecode_requests$_internal_utils, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"requests.adapters", modulecode_requests$adapters, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"requests.api", modulecode_requests$api, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"requests.auth", modulecode_requests$auth, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"requests.certs", modulecode_requests$certs, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"requests.compat", modulecode_requests$compat, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"requests.cookies", modulecode_requests$cookies, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"requests.exceptions", modulecode_requests$exceptions, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"requests.hooks", modulecode_requests$hooks, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"requests.models", modulecode_requests$models, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"requests.packages", modulecode_requests$packages, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"requests.sessions", modulecode_requests$sessions, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"requests.status_codes", modulecode_requests$status_codes, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"requests.structures", modulecode_requests$structures, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"requests.utils", modulecode_requests$utils, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"select", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"setuptools", NULL, 145, 8534, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"setuptools._deprecation_warning", NULL, 146, 544, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"setuptools._imp", NULL, 147, 2079, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"setuptools.command", NULL, 148, 371, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"setuptools.command.bdist_egg", NULL, 149, 13031, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"setuptools.command.egg_info", NULL, 150, 21972, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"setuptools.command.py36compat", NULL, 151, 4583, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"setuptools.command.sdist", NULL, 152, 6458, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"setuptools.command.setopt", NULL, 153, 4668, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"setuptools.config", NULL, 154, 20820, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"setuptools.depends", NULL, 155, 5243, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"setuptools.dist", NULL, 156, 36441, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"setuptools.extension", NULL, 157, 1938, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"setuptools.extern", NULL, 158, 2913, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"setuptools.glob", NULL, 159, 3688, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"setuptools.installer", NULL, 160, 2765, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"setuptools.monkey", NULL, 161, 4607, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"setuptools.py34compat", NULL, 162, 474, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"setuptools.unicode_utils", NULL, 163, 1108, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"setuptools.version", NULL, 164, 279, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"setuptools.wheel", NULL, 165, 7274, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"setuptools.windows_support", NULL, 166, 1017, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"six", modulecode_six, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"stack_data", modulecode_stack_data, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"stack_data.core", modulecode_stack_data$core, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"stack_data.formatting", modulecode_stack_data$formatting, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"stack_data.utils", modulecode_stack_data$utils, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"stack_data.version", modulecode_stack_data$version, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"tomli", modulecode_tomli, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"tomli._parser", modulecode_tomli$_parser, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"tomli._re", modulecode_tomli$_re, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"tomli._types", modulecode_tomli$_types, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"tornado", modulecode_tornado, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"tornado.concurrent", modulecode_tornado$concurrent, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"tornado.escape", modulecode_tornado$escape, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"tornado.gen", modulecode_tornado$gen, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"tornado.ioloop", modulecode_tornado$ioloop, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"tornado.iostream", modulecode_tornado$iostream, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"tornado.locks", modulecode_tornado$locks, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"tornado.log", modulecode_tornado$log, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"tornado.netutil", modulecode_tornado$netutil, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"tornado.options", modulecode_tornado$options, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"tornado.platform", modulecode_tornado$platform, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"tornado.platform.asyncio", modulecode_tornado$platform$asyncio, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"tornado.process", modulecode_tornado$process, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"tornado.queues", modulecode_tornado$queues, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"tornado.speedups", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"tornado.util", modulecode_tornado$util, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"traitlets", modulecode_traitlets, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"traitlets._version", modulecode_traitlets$_version, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"traitlets.config", modulecode_traitlets$config, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"traitlets.config.application", modulecode_traitlets$config$application, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"traitlets.config.configurable", modulecode_traitlets$config$configurable, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"traitlets.config.loader", modulecode_traitlets$config$loader, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"traitlets.log", modulecode_traitlets$log, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"traitlets.traitlets", modulecode_traitlets$traitlets, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"traitlets.utils", modulecode_traitlets$utils, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"traitlets.utils.bunch", modulecode_traitlets$utils$bunch, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"traitlets.utils.decorators", modulecode_traitlets$utils$decorators, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"traitlets.utils.descriptions", modulecode_traitlets$utils$descriptions, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"traitlets.utils.getargspec", modulecode_traitlets$utils$getargspec, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"traitlets.utils.importstring", modulecode_traitlets$utils$importstring, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"traitlets.utils.sentinel", modulecode_traitlets$utils$sentinel, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"traitlets.utils.text", modulecode_traitlets$utils$text, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"typing_extensions", modulecode_typing_extensions, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"unicodedata", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"urllib3", modulecode_urllib3, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"urllib3._collections", modulecode_urllib3$_collections, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"urllib3._version", modulecode_urllib3$_version, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"urllib3.connection", modulecode_urllib3$connection, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"urllib3.connectionpool", modulecode_urllib3$connectionpool, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"urllib3.contrib", modulecode_urllib3$contrib, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"urllib3.contrib._appengine_environ", modulecode_urllib3$contrib$_appengine_environ, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"urllib3.contrib.appengine", modulecode_urllib3$contrib$appengine, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"urllib3.contrib.pyopenssl", modulecode_urllib3$contrib$pyopenssl, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"urllib3.contrib.socks", modulecode_urllib3$contrib$socks, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"urllib3.exceptions", modulecode_urllib3$exceptions, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"urllib3.fields", modulecode_urllib3$fields, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"urllib3.filepost", modulecode_urllib3$filepost, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"urllib3.packages", modulecode_urllib3$packages, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"urllib3.packages.backports", modulecode_urllib3$packages$backports, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"urllib3.packages.backports.makefile", modulecode_urllib3$packages$backports$makefile, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"urllib3.packages.six", modulecode_urllib3$packages$six, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"urllib3.poolmanager", modulecode_urllib3$poolmanager, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"urllib3.request", modulecode_urllib3$request, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"urllib3.response", modulecode_urllib3$response, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"urllib3.util", modulecode_urllib3$util, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"urllib3.util.connection", modulecode_urllib3$util$connection, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"urllib3.util.proxy", modulecode_urllib3$util$proxy, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"urllib3.util.queue", modulecode_urllib3$util$queue, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"urllib3.util.request", modulecode_urllib3$util$request, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"urllib3.util.response", modulecode_urllib3$util$response, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"urllib3.util.retry", modulecode_urllib3$util$retry, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"urllib3.util.ssl_", modulecode_urllib3$util$ssl_, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"urllib3.util.ssl_match_hostname", modulecode_urllib3$util$ssl_match_hostname, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"urllib3.util.ssltransport", modulecode_urllib3$util$ssltransport, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"urllib3.util.timeout", modulecode_urllib3$util$timeout, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"urllib3.util.url", modulecode_urllib3$util$url, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"urllib3.util.wait", modulecode_urllib3$util$wait, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"wcwidth", modulecode_wcwidth, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"wcwidth.table_wide", modulecode_wcwidth$table_wide, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"wcwidth.table_zero", modulecode_wcwidth$table_zero, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"wcwidth.unicode_versions", modulecode_wcwidth$unicode_versions, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"wcwidth.wcwidth", modulecode_wcwidth$wcwidth, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"win32api", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"win32clipboard", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"win32com", modulecode_win32com, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"win32com.shell", modulecode_win32com$shell, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"win32com.shell.shell", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"win32com.shell.shellcon", modulecode_win32com$shell$shellcon, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"win32security", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"zmq", modulecode_zmq, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"zmq._future", modulecode_zmq$_future, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.asyncio", modulecode_zmq$asyncio, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.backend", modulecode_zmq$backend, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"zmq.backend.cython", modulecode_zmq$backend$cython, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"zmq.backend.cython._device", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"zmq.backend.cython._poll", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"zmq.backend.cython._proxy_steerable", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"zmq.backend.cython._version", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"zmq.backend.cython.constants", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"zmq.backend.cython.context", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"zmq.backend.cython.error", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"zmq.backend.cython.message", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"zmq.backend.cython.socket", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"zmq.backend.cython.utils", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_SHLIB_FLAG},
    {"zmq.backend.select", modulecode_zmq$backend$select, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.error", modulecode_zmq$error, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.eventloop", modulecode_zmq$eventloop, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"zmq.eventloop._deprecated", modulecode_zmq$eventloop$_deprecated, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.eventloop.ioloop", modulecode_zmq$eventloop$ioloop, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.eventloop.minitornado", modulecode_zmq$eventloop$minitornado, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"zmq.eventloop.minitornado.concurrent", modulecode_zmq$eventloop$minitornado$concurrent, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.eventloop.minitornado.ioloop", modulecode_zmq$eventloop$minitornado$ioloop, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.eventloop.minitornado.log", modulecode_zmq$eventloop$minitornado$log, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.eventloop.minitornado.platform", modulecode_zmq$eventloop$minitornado$platform, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"zmq.eventloop.minitornado.platform.auto", modulecode_zmq$eventloop$minitornado$platform$auto, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.eventloop.minitornado.platform.common", modulecode_zmq$eventloop$minitornado$platform$common, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.eventloop.minitornado.platform.interface", modulecode_zmq$eventloop$minitornado$platform$interface, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.eventloop.minitornado.platform.posix", modulecode_zmq$eventloop$minitornado$platform$posix, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.eventloop.minitornado.platform.windows", modulecode_zmq$eventloop$minitornado$platform$windows, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.eventloop.minitornado.stack_context", modulecode_zmq$eventloop$minitornado$stack_context, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.eventloop.minitornado.util", modulecode_zmq$eventloop$minitornado$util, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.eventloop.zmqstream", modulecode_zmq$eventloop$zmqstream, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.sugar", modulecode_zmq$sugar, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"zmq.sugar.attrsettr", modulecode_zmq$sugar$attrsettr, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.sugar.constants", modulecode_zmq$sugar$constants, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.sugar.context", modulecode_zmq$sugar$context, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.sugar.frame", modulecode_zmq$sugar$frame, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.sugar.poll", modulecode_zmq$sugar$poll, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.sugar.socket", modulecode_zmq$sugar$socket, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.sugar.stopwatch", modulecode_zmq$sugar$stopwatch, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.sugar.tracker", modulecode_zmq$sugar$tracker, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.sugar.version", modulecode_zmq$sugar$version, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.utils", modulecode_zmq$utils, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"zmq.utils.constant_names", modulecode_zmq$utils$constant_names, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.utils.interop", modulecode_zmq$utils$interop, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.utils.jsonapi", modulecode_zmq$utils$jsonapi, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"zmq.utils.strtypes", modulecode_zmq$utils$strtypes, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"__future__", NULL, 167, 4089, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_aix_support", NULL, 168, 3009, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_bootlocale", NULL, 169, 1190, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_bootsubprocess", NULL, 170, 2208, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_collections_abc", NULL, 171, 31701, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_compat_pickle", NULL, 172, 5451, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_compression", NULL, 173, 4161, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_markupbase", NULL, 174, 7734, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_osx_support", NULL, 175, 11545, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_py_abc", NULL, 176, 4619, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_pyio", NULL, 177, 74446, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_sitebuiltins", NULL, 178, 3464, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_strptime", NULL, 179, 15978, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_threading_local", NULL, 180, 6469, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_weakrefset", NULL, 181, 7687, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"abc", NULL, 182, 5738, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"aifc", NULL, 183, 25229, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"argparse", NULL, 184, 63404, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"ast", NULL, 185, 52269, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asynchat", NULL, 186, 6785, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio", NULL, 187, 735, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"asyncio.base_events", NULL, 188, 51963, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.base_futures", NULL, 189, 1873, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.base_subprocess", NULL, 190, 9375, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.base_tasks", NULL, 191, 1909, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.constants", NULL, 192, 546, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.coroutines", NULL, 193, 6602, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.events", NULL, 194, 28066, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.exceptions", NULL, 195, 2518, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.format_helpers", NULL, 196, 2289, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.futures", NULL, 197, 11794, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.locks", NULL, 198, 14394, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.log", NULL, 199, 191, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.proactor_events", NULL, 200, 24314, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.protocols", NULL, 201, 8579, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.queues", NULL, 202, 8481, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.runners", NULL, 203, 2172, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.selector_events", NULL, 204, 29796, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.sslproto", NULL, 205, 21521, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.staggered", NULL, 206, 4125, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.streams", NULL, 207, 20551, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.subprocess", NULL, 208, 7300, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.tasks", NULL, 209, 24304, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.threads", NULL, 210, 943, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.transports", NULL, 211, 12211, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.trsock", NULL, 212, 8534, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.windows_events", NULL, 213, 24600, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.windows_utils", NULL, 214, 4468, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncore", NULL, 215, 15999, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"base64", NULL, 216, 16418, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"bdb", NULL, 217, 24503, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"binhex", NULL, 218, 12928, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"bisect", NULL, 219, 2313, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"bz2", NULL, 220, 11508, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"cProfile", NULL, 221, 5058, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"calendar", NULL, 222, 26994, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"cgi", NULL, 223, 26445, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"cgitb", NULL, 224, 10149, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"chunk", NULL, 225, 4804, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"cmd", NULL, 226, 12639, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"code", NULL, 227, 9879, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"codecs", NULL, 228, 33851, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"codeop", NULL, 229, 6421, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"collections", NULL, 230, 48055, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"collections.abc", NULL, 231, 31700, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"colorsys", NULL, 232, 3223, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"compileall", NULL, 233, 12552, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"concurrent", NULL, 234, 88, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"concurrent.futures", NULL, 235, 1064, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"concurrent.futures._base", NULL, 236, 22287, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"concurrent.futures.process", NULL, 237, 20705, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"concurrent.futures.thread", NULL, 238, 5869, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"configparser", NULL, 239, 45832, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"contextlib", NULL, 240, 19501, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"contextvars", NULL, 241, 208, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"copy", NULL, 242, 6926, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"copyreg", NULL, 243, 4393, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"csv", NULL, 244, 11812, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"ctypes", NULL, 245, 16388, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"ctypes._aix", NULL, 246, 9799, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"ctypes._endian", NULL, 247, 1894, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"ctypes.macholib", NULL, 248, 255, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"ctypes.macholib.dyld", NULL, 249, 4621, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"ctypes.macholib.dylib", NULL, 250, 1865, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"ctypes.macholib.framework", NULL, 251, 2145, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"ctypes.util", NULL, 252, 8226, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"ctypes.wintypes", NULL, 253, 5068, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"dataclasses", NULL, 254, 23148, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"datetime", NULL, 255, 58060, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"dbm", NULL, 256, 4187, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"dbm.dumb", NULL, 257, 7878, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"decimal", NULL, 258, 160573, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"difflib", NULL, 259, 58543, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"dis", NULL, 260, 15783, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils", NULL, 261, 340, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"distutils._msvccompiler", NULL, 262, 12790, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.archive_util", NULL, 263, 6550, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.bcppcompiler", NULL, 264, 6461, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.ccompiler", NULL, 265, 33151, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.cmd", NULL, 266, 13889, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.command", NULL, 267, 429, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"distutils.command.bdist", NULL, 268, 3568, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.command.bdist_dumb", NULL, 269, 3551, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.command.bdist_msi", NULL, 270, 19733, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.command.bdist_rpm", NULL, 271, 12188, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.command.bdist_wininst", NULL, 272, 8508, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.command.build", NULL, 273, 3844, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.command.build_clib", NULL, 274, 4763, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.command.build_ext", NULL, 275, 16154, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.command.build_py", NULL, 276, 10396, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.command.build_scripts", NULL, 277, 4293, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.command.check", NULL, 278, 4871, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.command.clean", NULL, 279, 2045, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.command.config", NULL, 280, 10175, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.command.install", NULL, 281, 13503, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.command.install_data", NULL, 282, 2248, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.command.install_egg_info", NULL, 283, 2983, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.command.install_headers", NULL, 284, 1673, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.command.install_lib", NULL, 285, 5045, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.command.install_scripts", NULL, 286, 2096, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.command.register", NULL, 287, 8416, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.command.sdist", NULL, 288, 14443, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.command.upload", NULL, 289, 5192, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.config", NULL, 290, 3492, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.core", NULL, 291, 6617, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.cygwinccompiler", NULL, 292, 8466, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.debug", NULL, 293, 159, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.dep_util", NULL, 294, 2679, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.dir_util", NULL, 295, 5780, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.dist", NULL, 296, 34311, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.errors", NULL, 297, 5215, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.extension", NULL, 298, 6880, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.fancy_getopt", NULL, 299, 10588, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.file_util", NULL, 300, 5946, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.filelist", NULL, 301, 9798, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.log", NULL, 302, 2278, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.msvc9compiler", NULL, 303, 17475, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.msvccompiler", NULL, 304, 14670, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.spawn", NULL, 305, 3404, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.sysconfig", NULL, 306, 12024, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.text_file", NULL, 307, 8404, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.unixccompiler", NULL, 308, 6770, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.util", NULL, 309, 15553, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.version", NULL, 310, 7304, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"distutils.versionpredicate", NULL, 311, 5088, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"doctest", NULL, 312, 75941, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email", NULL, 313, 1621, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"email._encoded_words", NULL, 314, 5645, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email._header_value_parser", NULL, 315, 79746, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email._parseaddr", NULL, 316, 12356, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email._policybase", NULL, 317, 14771, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.base64mime", NULL, 318, 3202, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.charset", NULL, 319, 11416, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.contentmanager", NULL, 320, 7323, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.encoders", NULL, 321, 1585, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.errors", NULL, 322, 5874, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.feedparser", NULL, 323, 10572, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.generator", NULL, 324, 12548, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.header", NULL, 325, 16395, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.headerregistry", NULL, 326, 21929, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.iterators", NULL, 327, 1894, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.message", NULL, 328, 37799, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.mime", NULL, 329, 88, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"email.mime.application", NULL, 330, 1424, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.mime.audio", NULL, 331, 2589, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.mime.base", NULL, 332, 1010, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.mime.image", NULL, 333, 1869, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.mime.message", NULL, 334, 1247, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.mime.multipart", NULL, 335, 1467, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.mime.nonmultipart", NULL, 336, 729, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.mime.text", NULL, 337, 1274, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.parser", NULL, 338, 5709, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.policy", NULL, 339, 9602, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.quoprimime", NULL, 340, 7637, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.utils", NULL, 341, 9550, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings", NULL, 342, 3851, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"encodings.aliases", NULL, 343, 6293, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.ascii", NULL, 344, 1846, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.base64_codec", NULL, 345, 2333, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.big5", NULL, 346, 1374, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.big5hkscs", NULL, 347, 1384, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.bz2_codec", NULL, 348, 3222, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.charmap", NULL, 349, 2856, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp037", NULL, 350, 2387, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp1006", NULL, 351, 2463, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp1026", NULL, 352, 2391, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp1125", NULL, 353, 8094, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp1140", NULL, 354, 2377, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp1250", NULL, 355, 2414, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp1251", NULL, 356, 2411, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp1252", NULL, 357, 2414, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp1253", NULL, 358, 2427, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp1254", NULL, 359, 2416, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp1255", NULL, 360, 2435, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp1256", NULL, 361, 2413, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp1257", NULL, 362, 2421, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp1258", NULL, 363, 2419, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp273", NULL, 364, 2373, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp424", NULL, 365, 2417, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp437", NULL, 366, 7811, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp500", NULL, 367, 2387, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp720", NULL, 368, 2484, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp737", NULL, 369, 8133, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp775", NULL, 370, 7841, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp850", NULL, 371, 7472, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp852", NULL, 372, 7849, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp855", NULL, 373, 8102, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp856", NULL, 374, 2449, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp857", NULL, 375, 7452, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp858", NULL, 376, 7442, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp860", NULL, 377, 7790, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp861", NULL, 378, 7805, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp862", NULL, 379, 7994, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp863", NULL, 380, 7805, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp864", NULL, 381, 7949, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp865", NULL, 382, 7805, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp866", NULL, 383, 8138, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp869", NULL, 384, 7829, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp874", NULL, 385, 2515, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp875", NULL, 386, 2384, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp932", NULL, 387, 1376, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp949", NULL, 388, 1376, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp950", NULL, 389, 1376, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.euc_jis_2004", NULL, 390, 1390, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.euc_jisx0213", NULL, 391, 1390, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.euc_jp", NULL, 392, 1378, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.euc_kr", NULL, 393, 1378, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.gb18030", NULL, 394, 1380, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.gb2312", NULL, 395, 1378, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.gbk", NULL, 396, 1372, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.hex_codec", NULL, 397, 2320, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.hp_roman8", NULL, 398, 2588, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.hz", NULL, 399, 1370, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.idna", NULL, 400, 5562, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso2022_jp", NULL, 401, 1391, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso2022_jp_1", NULL, 402, 1395, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso2022_jp_2", NULL, 403, 1395, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso2022_jp_2004", NULL, 404, 1401, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso2022_jp_3", NULL, 405, 1395, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso2022_jp_ext", NULL, 406, 1399, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso2022_kr", NULL, 407, 1391, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_1", NULL, 408, 2386, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_10", NULL, 409, 2391, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_11", NULL, 410, 2485, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_13", NULL, 411, 2394, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_14", NULL, 412, 2412, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_15", NULL, 413, 2391, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_16", NULL, 414, 2393, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_2", NULL, 415, 2386, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_3", NULL, 416, 2393, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_4", NULL, 417, 2386, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_5", NULL, 418, 2387, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_6", NULL, 419, 2431, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_7", NULL, 420, 2394, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_8", NULL, 421, 2425, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_9", NULL, 422, 2386, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.johab", NULL, 423, 1376, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.koi8_r", NULL, 424, 2438, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.koi8_t", NULL, 425, 2349, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.koi8_u", NULL, 426, 2424, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.kz1048", NULL, 427, 2401, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.latin_1", NULL, 428, 1858, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.mac_arabic", NULL, 429, 7705, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.mac_croatian", NULL, 430, 2433, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.mac_cyrillic", NULL, 431, 2423, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.mac_farsi", NULL, 432, 2367, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.mac_greek", NULL, 433, 2407, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.mac_iceland", NULL, 434, 2426, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.mac_latin2", NULL, 435, 2567, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.mac_roman", NULL, 436, 2424, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.mac_romanian", NULL, 437, 2434, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.mac_turkish", NULL, 438, 2427, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.mbcs", NULL, 439, 1676, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.oem", NULL, 440, 1489, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.palmos", NULL, 441, 2414, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.ptcp154", NULL, 442, 2508, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.punycode", NULL, 443, 6272, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.quopri_codec", NULL, 444, 2359, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.raw_unicode_escape", NULL, 445, 1938, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.rot_13", NULL, 446, 2966, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.shift_jis", NULL, 447, 1384, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.shift_jis_2004", NULL, 448, 1394, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.shift_jisx0213", NULL, 449, 1394, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.tis_620", NULL, 450, 2476, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.undefined", NULL, 451, 2060, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.unicode_escape", NULL, 452, 1918, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.utf_16", NULL, 453, 4835, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.utf_16_be", NULL, 454, 1615, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.utf_16_le", NULL, 455, 1615, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.utf_32", NULL, 456, 4728, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.utf_32_be", NULL, 457, 1508, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.utf_32_le", NULL, 458, 1508, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.utf_7", NULL, 459, 1536, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.utf_8", NULL, 460, 1595, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.utf_8_sig", NULL, 461, 4507, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.uu_codec", NULL, 462, 3195, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.zlib_codec", NULL, 463, 3043, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"enum", NULL, 464, 25983, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"filecmp", NULL, 465, 8585, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"fileinput", NULL, 466, 13753, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"fnmatch", NULL, 467, 3905, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"formatter", NULL, 468, 17502, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"fractions", NULL, 469, 18012, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"ftplib", NULL, 470, 28657, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"functools", NULL, 471, 28393, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"genericpath", NULL, 472, 3987, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"getopt", NULL, 473, 6223, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"getpass", NULL, 474, 4163, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"gettext", NULL, 475, 18036, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"glob", NULL, 476, 4507, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"graphlib", NULL, 477, 7531, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"gzip", NULL, 478, 18457, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"hashlib", NULL, 479, 6654, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"heapq", NULL, 480, 14003, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"hmac", NULL, 481, 6763, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"html", NULL, 482, 3079, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"html.entities", NULL, 483, 50484, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"html.parser", NULL, 484, 10818, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"http", NULL, 485, 6367, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"http.client", NULL, 486, 35502, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"http.cookiejar", NULL, 487, 53468, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"http.cookies", NULL, 488, 15253, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"http.server", NULL, 489, 34377, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"imaplib", NULL, 490, 42375, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"imghdr", NULL, 491, 4103, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"imp", NULL, 492, 9814, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"importlib", NULL, 493, 3787, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"importlib._bootstrap", NULL, 494, 28931, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"importlib._bootstrap_external", NULL, 495, 45133, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"importlib._common", NULL, 496, 1662, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"importlib.abc", NULL, 497, 16780, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"importlib.machinery", NULL, 498, 927, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"importlib.metadata", NULL, 499, 21584, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"importlib.resources", NULL, 500, 6354, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"importlib.util", NULL, 501, 9285, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"inspect", NULL, 502, 81435, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"io", NULL, 503, 3371, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"ipaddress", NULL, 504, 62456, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"json", NULL, 505, 12247, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"json.decoder", NULL, 506, 9771, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"json.encoder", NULL, 507, 11094, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"json.scanner", NULL, 508, 1916, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"json.tool", NULL, 509, 2772, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"keyword", NULL, 510, 879, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3", NULL, 511, 256, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"lib2to3.btm_matcher", NULL, 512, 4840, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.btm_utils", NULL, 513, 6111, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixer_base", NULL, 514, 6218, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixer_util", NULL, 515, 12133, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes", NULL, 516, 91, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"lib2to3.fixes.fix_apply", NULL, 517, 1622, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_asserts", NULL, 518, 1237, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_basestring", NULL, 519, 621, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_buffer", NULL, 520, 766, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_dict", NULL, 521, 3269, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_except", NULL, 522, 2764, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_exec", NULL, 523, 1091, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_execfile", NULL, 524, 1639, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_exitfunc", NULL, 525, 2264, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_filter", NULL, 526, 2400, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_funcattrs", NULL, 527, 934, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_future", NULL, 528, 742, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_getcwdu", NULL, 529, 746, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_has_key", NULL, 530, 2861, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_idioms", NULL, 531, 3863, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_import", NULL, 532, 2741, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_imports", NULL, 533, 4345, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_imports2", NULL, 534, 504, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_input", NULL, 535, 908, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_intern", NULL, 536, 1092, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_isinstance", NULL, 537, 1509, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_itertools", NULL, 538, 1508, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_itertools_imports", NULL, 539, 1520, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_long", NULL, 540, 663, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_map", NULL, 541, 3055, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_metaclass", NULL, 542, 5289, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_methodattrs", NULL, 543, 896, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_ne", NULL, 544, 769, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_next", NULL, 545, 3013, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_nonzero", NULL, 546, 881, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_numliterals", NULL, 547, 981, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_operator", NULL, 548, 4178, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_paren", NULL, 549, 1347, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_print", NULL, 550, 2281, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_raise", NULL, 551, 2207, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_raw_input", NULL, 552, 753, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_reduce", NULL, 553, 1086, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_reload", NULL, 554, 1104, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_renames", NULL, 555, 1961, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_repr", NULL, 556, 803, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_set_literal", NULL, 557, 1637, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_standarderror", NULL, 558, 678, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_sys_exc", NULL, 559, 1365, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_throw", NULL, 560, 1762, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_tuple_params", NULL, 561, 4539, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_types", NULL, 562, 1791, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_unicode", NULL, 563, 1507, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_urllib", NULL, 564, 5818, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_ws_comma", NULL, 565, 1077, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_xrange", NULL, 566, 2487, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_xreadlines", NULL, 567, 1077, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_zip", NULL, 568, 1537, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.main", NULL, 569, 8652, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.patcomp", NULL, 570, 5568, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.pgen2", NULL, 571, 121, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"lib2to3.pgen2.driver", NULL, 572, 5092, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.pgen2.grammar", NULL, 573, 5670, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.pgen2.literals", NULL, 574, 1494, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.pgen2.parse", NULL, 575, 6443, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.pgen2.pgen", NULL, 576, 9685, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.pgen2.token", NULL, 577, 1852, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.pgen2.tokenize", NULL, 578, 15136, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.pygram", NULL, 579, 1225, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.pytree", NULL, 580, 24258, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lib2to3.refactor", NULL, 581, 20606, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"linecache", NULL, 582, 3991, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"locale", NULL, 583, 34659, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"logging", NULL, 584, 66282, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"logging.config", NULL, 585, 23220, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"logging.handlers", NULL, 586, 44018, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lzma", NULL, 587, 12057, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"mailbox", NULL, 588, 60563, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"mailcap", NULL, 589, 6472, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"mimetypes", NULL, 590, 16015, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"modulefinder", NULL, 591, 16091, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"msilib", NULL, 592, 15836, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"msilib.schema", NULL, 593, 49593, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"msilib.sequence", NULL, 594, 2346, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"msilib.text", NULL, 595, 7957, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"multiprocessing", NULL, 596, 608, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"multiprocessing.connection", NULL, 597, 25623, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"multiprocessing.context", NULL, 598, 12983, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"multiprocessing.dummy", NULL, 599, 3819, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"multiprocessing.dummy.connection", NULL, 600, 2548, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"multiprocessing.forkserver", NULL, 601, 8380, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"multiprocessing.heap", NULL, 602, 7598, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"multiprocessing.managers", NULL, 603, 40880, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"multiprocessing.pool", NULL, 604, 25101, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"multiprocessing.popen_spawn_win32", NULL, 605, 3420, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"multiprocessing.process", NULL, 606, 10972, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"multiprocessing.queues", NULL, 607, 10157, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"multiprocessing.reduction", NULL, 608, 8248, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"multiprocessing.resource_sharer", NULL, 609, 5247, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"multiprocessing.resource_tracker", NULL, 610, 5420, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"multiprocessing.shared_memory", NULL, 611, 14405, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"multiprocessing.sharedctypes", NULL, 612, 7060, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"multiprocessing.spawn", NULL, 613, 6684, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"multiprocessing.synchronize", NULL, 614, 11351, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"multiprocessing.util", NULL, 615, 11470, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"netrc", NULL, 616, 3746, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"nntplib", NULL, 617, 31726, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"ntpath", NULL, 618, 14505, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"nturl2path", NULL, 619, 1709, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"numbers", NULL, 620, 12282, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"opcode", NULL, 621, 5186, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"operator", NULL, 622, 13747, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"optparse", NULL, 623, 47906, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"os", NULL, 624, 31609, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pathlib", NULL, 625, 44688, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pdb", NULL, 626, 47475, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pickle", NULL, 627, 47061, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pickletools", NULL, 628, 67070, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pipes", NULL, 629, 7758, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pkgutil", NULL, 630, 18529, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"platform", NULL, 631, 26379, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"plistlib", NULL, 632, 23510, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"poplib", NULL, 633, 13620, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"posixpath", NULL, 634, 10292, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pprint", NULL, 635, 16793, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"profile", NULL, 636, 14353, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pstats", NULL, 637, 23715, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"py_compile", NULL, 638, 7327, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pyclbr", NULL, 639, 10412, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pydoc", NULL, 640, 85279, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pydoc_data", NULL, 641, 88, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"pydoc_data.topics", NULL, 642, 430871, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"queue", NULL, 643, 10826, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"quopri", NULL, 644, 5710, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"random", NULL, 645, 22006, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"re", NULL, 646, 14325, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"reprlib", NULL, 647, 5270, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"rlcompleter", NULL, 648, 5769, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"runpy", NULL, 649, 8472, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"sched", NULL, 650, 6596, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"secrets", NULL, 651, 2143, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"selectors", NULL, 652, 17208, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"shelve", NULL, 653, 9507, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"shlex", NULL, 654, 7697, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"shutil", NULL, 655, 37979, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"signal", NULL, 656, 2786, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"site", NULL, 657, 13817, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"smtpd", NULL, 658, 26487, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"smtplib", NULL, 659, 35893, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"sndhdr", NULL, 660, 6956, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"socket", NULL, 661, 29136, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"socketserver", NULL, 662, 25478, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"sqlite3", NULL, 663, 1136, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"sqlite3.dbapi2", NULL, 664, 2461, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"sqlite3.dump", NULL, 665, 1886, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"sre_compile", NULL, 666, 15016, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"sre_constants", NULL, 667, 6280, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"sre_parse", NULL, 668, 21566, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"ssl", NULL, 669, 44555, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"stat", NULL, 670, 4335, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"statistics", NULL, 671, 31942, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"string", NULL, 672, 7128, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"stringprep", NULL, 673, 9949, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"struct", NULL, 674, 269, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"subprocess", NULL, 675, 44109, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"sunau", NULL, 676, 16780, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"symbol", NULL, 677, 2542, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"symtable", NULL, 678, 11129, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"sysconfig", NULL, 679, 16030, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"tabnanny", NULL, 680, 7028, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"tarfile", NULL, 681, 63207, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"telnetlib", NULL, 682, 18294, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"tempfile", NULL, 683, 23378, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"textwrap", NULL, 684, 13484, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"this", NULL, 685, 1222, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"threading", NULL, 686, 42141, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"timeit", NULL, 687, 11719, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"tkinter", NULL, 688, 176002, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"tkinter.colorchooser", NULL, 689, 2238, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"tkinter.commondialog", NULL, 690, 1141, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"tkinter.constants", NULL, 691, 1619, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"tkinter.dialog", NULL, 692, 1462, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"tkinter.dnd", NULL, 693, 11250, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"tkinter.filedialog", NULL, 694, 12581, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"tkinter.font", NULL, 695, 6345, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"tkinter.messagebox", NULL, 696, 3045, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"tkinter.scrolledtext", NULL, 697, 2146, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"tkinter.simpledialog", NULL, 698, 10973, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"tkinter.tix", NULL, 699, 79230, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"tkinter.ttk", NULL, 700, 56843, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"token", NULL, 701, 2459, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"tokenize", NULL, 702, 17128, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"trace", NULL, 703, 19702, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"traceback", NULL, 704, 20364, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"tracemalloc", NULL, 705, 17898, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"turtle", NULL, 706, 129499, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"types", NULL, 707, 9184, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"typing", NULL, 708, 71808, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"unittest", NULL, 709, 3352, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"unittest._log", NULL, 710, 2486, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"unittest.async_case", NULL, 711, 4668, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"unittest.case", NULL, 712, 48121, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"unittest.loader", NULL, 713, 14481, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"unittest.main", NULL, 714, 7475, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"unittest.mock", NULL, 715, 77977, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"unittest.result", NULL, 716, 7254, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"unittest.runner", NULL, 717, 7029, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"unittest.signals", NULL, 718, 2205, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"unittest.suite", NULL, 719, 10067, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"unittest.util", NULL, 720, 4401, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"urllib", NULL, 721, 84, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"urllib.error", NULL, 722, 2789, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"urllib.parse", NULL, 723, 34848, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"urllib.request", NULL, 724, 72210, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"urllib.response", NULL, 725, 3419, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"urllib.robotparser", NULL, 726, 7290, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"uu", NULL, 727, 3629, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"uuid", NULL, 728, 22473, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"venv", NULL, 729, 15474, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"warnings", NULL, 730, 13568, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"wave", NULL, 731, 17836, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"weakref", NULL, 732, 20248, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"webbrowser", NULL, 733, 17097, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"wsgiref", NULL, 734, 680, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"wsgiref.handlers", NULL, 735, 16339, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"wsgiref.headers", NULL, 736, 7697, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"wsgiref.simple_server", NULL, 737, 5264, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"wsgiref.util", NULL, 738, 5358, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"wsgiref.validate", NULL, 739, 14720, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xdrlib", NULL, 740, 8206, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml", NULL, 741, 646, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"xml.dom", NULL, 742, 5492, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"xml.dom.NodeFilter", NULL, 743, 932, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.dom.domreg", NULL, 744, 2813, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.dom.expatbuilder", NULL, 745, 27273, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.dom.minicompat", NULL, 746, 2704, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.dom.minidom", NULL, 747, 56274, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.dom.pulldom", NULL, 748, 10654, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.dom.xmlbuilder", NULL, 749, 12440, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.etree", NULL, 750, 87, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"xml.etree.ElementInclude", NULL, 751, 2397, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.etree.ElementPath", NULL, 752, 8377, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.etree.ElementTree", NULL, 753, 56203, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.etree.cElementTree", NULL, 754, 138, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.parsers", NULL, 755, 261, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"xml.parsers.expat", NULL, 756, 299, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.sax", NULL, 757, 3154, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"xml.sax._exceptions", NULL, 758, 5409, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.sax.expatreader", NULL, 759, 12545, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.sax.handler", NULL, 760, 12387, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.sax.saxutils", NULL, 761, 12886, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.sax.xmlreader", NULL, 762, 16809, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xmlrpc", NULL, 763, 84, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"xmlrpc.client", NULL, 764, 34677, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xmlrpc.server", NULL, 765, 29338, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"zipapp", NULL, 766, 5948, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"zipfile", NULL, 767, 58857, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"zoneinfo", NULL, 768, 765, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"zoneinfo._common", NULL, 769, 3069, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"zoneinfo._tzpath", NULL, 770, 4010, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"zoneinfo._zoneinfo", NULL, 771, 15431, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {NULL, NULL, 0, 0, 0}
};

static void _loadBytesCodesBlob()
{
    static bool init_done = false;

    if (init_done == false) {
        loadConstantsBlob((PyObject **)bytecode_data, ".bytecode");

        init_done = true;
    }
}


void setupMetaPathBasedLoader(void) {
    static bool init_done = false;
    if (init_done == false) {
        _loadBytesCodesBlob();
        registerMetaPathBasedUnfreezer(meta_path_loader_entries, bytecode_data);

        init_done = true;
    }


}

// This provides the frozen (compiled bytecode) files that are included if
// any.

// These modules should be loaded as bytecode. They may e.g. have to be loadable
// during "Py_Initialize" already, or for irrelevance, they are only included
// in this un-optimized form. These are not compiled by Nuitka, and therefore
// are not accelerated at all, merely bundled with the binary or module, so
// that CPython library can start out finding them.

struct frozen_desc {
    char const *name;
    int index;
    int size;
};

static struct frozen_desc _frozen_modules[] = {
    {"_collections_abc", 171, 31701},
    {"_compression", 173, 4161},
    {"_weakrefset", 181, 7687},
    {"abc", 182, 5738},
    {"ast", 185, 52269},
    {"base64", 216, 16418},
    {"bz2", 220, 11508},
    {"codecs", 228, 33851},
    {"collections", 230, -48055},
    {"collections.abc", 231, 31700},
    {"contextlib", 240, 19501},
    {"copyreg", 243, 4393},
    {"dis", 260, 15783},
    {"encodings", 342, -3851},
    {"encodings.aliases", 343, 6293},
    {"encodings.ascii", 344, 1846},
    {"encodings.base64_codec", 345, 2333},
    {"encodings.big5", 346, 1374},
    {"encodings.big5hkscs", 347, 1384},
    {"encodings.bz2_codec", 348, 3222},
    {"encodings.charmap", 349, 2856},
    {"encodings.cp037", 350, 2387},
    {"encodings.cp1006", 351, 2463},
    {"encodings.cp1026", 352, 2391},
    {"encodings.cp1125", 353, 8094},
    {"encodings.cp1140", 354, 2377},
    {"encodings.cp1250", 355, 2414},
    {"encodings.cp1251", 356, 2411},
    {"encodings.cp1252", 357, 2414},
    {"encodings.cp1253", 358, 2427},
    {"encodings.cp1254", 359, 2416},
    {"encodings.cp1255", 360, 2435},
    {"encodings.cp1256", 361, 2413},
    {"encodings.cp1257", 362, 2421},
    {"encodings.cp1258", 363, 2419},
    {"encodings.cp273", 364, 2373},
    {"encodings.cp424", 365, 2417},
    {"encodings.cp437", 366, 7811},
    {"encodings.cp500", 367, 2387},
    {"encodings.cp720", 368, 2484},
    {"encodings.cp737", 369, 8133},
    {"encodings.cp775", 370, 7841},
    {"encodings.cp850", 371, 7472},
    {"encodings.cp852", 372, 7849},
    {"encodings.cp855", 373, 8102},
    {"encodings.cp856", 374, 2449},
    {"encodings.cp857", 375, 7452},
    {"encodings.cp858", 376, 7442},
    {"encodings.cp860", 377, 7790},
    {"encodings.cp861", 378, 7805},
    {"encodings.cp862", 379, 7994},
    {"encodings.cp863", 380, 7805},
    {"encodings.cp864", 381, 7949},
    {"encodings.cp865", 382, 7805},
    {"encodings.cp866", 383, 8138},
    {"encodings.cp869", 384, 7829},
    {"encodings.cp874", 385, 2515},
    {"encodings.cp875", 386, 2384},
    {"encodings.cp932", 387, 1376},
    {"encodings.cp949", 388, 1376},
    {"encodings.cp950", 389, 1376},
    {"encodings.euc_jis_2004", 390, 1390},
    {"encodings.euc_jisx0213", 391, 1390},
    {"encodings.euc_jp", 392, 1378},
    {"encodings.euc_kr", 393, 1378},
    {"encodings.gb18030", 394, 1380},
    {"encodings.gb2312", 395, 1378},
    {"encodings.gbk", 396, 1372},
    {"encodings.hex_codec", 397, 2320},
    {"encodings.hp_roman8", 398, 2588},
    {"encodings.hz", 399, 1370},
    {"encodings.idna", 400, 5562},
    {"encodings.iso2022_jp", 401, 1391},
    {"encodings.iso2022_jp_1", 402, 1395},
    {"encodings.iso2022_jp_2", 403, 1395},
    {"encodings.iso2022_jp_2004", 404, 1401},
    {"encodings.iso2022_jp_3", 405, 1395},
    {"encodings.iso2022_jp_ext", 406, 1399},
    {"encodings.iso2022_kr", 407, 1391},
    {"encodings.iso8859_1", 408, 2386},
    {"encodings.iso8859_10", 409, 2391},
    {"encodings.iso8859_11", 410, 2485},
    {"encodings.iso8859_13", 411, 2394},
    {"encodings.iso8859_14", 412, 2412},
    {"encodings.iso8859_15", 413, 2391},
    {"encodings.iso8859_16", 414, 2393},
    {"encodings.iso8859_2", 415, 2386},
    {"encodings.iso8859_3", 416, 2393},
    {"encodings.iso8859_4", 417, 2386},
    {"encodings.iso8859_5", 418, 2387},
    {"encodings.iso8859_6", 419, 2431},
    {"encodings.iso8859_7", 420, 2394},
    {"encodings.iso8859_8", 421, 2425},
    {"encodings.iso8859_9", 422, 2386},
    {"encodings.johab", 423, 1376},
    {"encodings.koi8_r", 424, 2438},
    {"encodings.koi8_t", 425, 2349},
    {"encodings.koi8_u", 426, 2424},
    {"encodings.kz1048", 427, 2401},
    {"encodings.latin_1", 428, 1858},
    {"encodings.mac_arabic", 429, 7705},
    {"encodings.mac_croatian", 430, 2433},
    {"encodings.mac_cyrillic", 431, 2423},
    {"encodings.mac_farsi", 432, 2367},
    {"encodings.mac_greek", 433, 2407},
    {"encodings.mac_iceland", 434, 2426},
    {"encodings.mac_latin2", 435, 2567},
    {"encodings.mac_roman", 436, 2424},
    {"encodings.mac_romanian", 437, 2434},
    {"encodings.mac_turkish", 438, 2427},
    {"encodings.mbcs", 439, 1676},
    {"encodings.oem", 440, 1489},
    {"encodings.palmos", 441, 2414},
    {"encodings.ptcp154", 442, 2508},
    {"encodings.punycode", 443, 6272},
    {"encodings.quopri_codec", 444, 2359},
    {"encodings.raw_unicode_escape", 445, 1938},
    {"encodings.rot_13", 446, 2966},
    {"encodings.shift_jis", 447, 1384},
    {"encodings.shift_jis_2004", 448, 1394},
    {"encodings.shift_jisx0213", 449, 1394},
    {"encodings.tis_620", 450, 2476},
    {"encodings.undefined", 451, 2060},
    {"encodings.unicode_escape", 452, 1918},
    {"encodings.utf_16", 453, 4835},
    {"encodings.utf_16_be", 454, 1615},
    {"encodings.utf_16_le", 455, 1615},
    {"encodings.utf_32", 456, 4728},
    {"encodings.utf_32_be", 457, 1508},
    {"encodings.utf_32_le", 458, 1508},
    {"encodings.utf_7", 459, 1536},
    {"encodings.utf_8", 460, 1595},
    {"encodings.utf_8_sig", 461, 4507},
    {"encodings.uu_codec", 462, 3195},
    {"encodings.zlib_codec", 463, 3043},
    {"enum", 464, 25983},
    {"functools", 471, 28393},
    {"genericpath", 472, 3987},
    {"heapq", 480, 14003},
    {"importlib", 493, -3787},
    {"importlib._bootstrap", 494, 28931},
    {"importlib._bootstrap_external", 495, 45133},
    {"importlib.machinery", 498, 927},
    {"inspect", 502, 81435},
    {"io", 503, 3371},
    {"keyword", 510, 879},
    {"linecache", 582, 3991},
    {"locale", 583, 34659},
    {"ntpath", 618, 14505},
    {"opcode", 621, 5186},
    {"operator", 622, 13747},
    {"os", 624, 31609},
    {"quopri", 644, 5710},
    {"re", 646, 14325},
    {"reprlib", 647, 5270},
    {"sre_compile", 666, 15016},
    {"sre_constants", 667, 6280},
    {"sre_parse", 668, 21566},
    {"stat", 670, 4335},
    {"stringprep", 673, 9949},
    {"struct", 674, 269},
    {"threading", 686, 42141},
    {"token", 701, 2459},
    {"tokenize", 702, 17128},
    {"types", 707, 9184},
    {"warnings", 730, 13568},
    {NULL, 0, 0}
};


void copyFrozenModulesTo(struct _frozen *destination) {
    _loadBytesCodesBlob();

    struct frozen_desc *current = _frozen_modules;

    for (;;) {
        destination->name = (char *)current->name;
        destination->code = bytecode_data[current->index];
        destination->size = current->size;

        if (destination->name == NULL) break;

        current += 1;
        destination += 1;
    };
}

