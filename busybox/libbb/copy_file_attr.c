/* vi: set sw=4 ts=4: */
/*
 * Copy extended attributes between files
 *
 * Copyright (C) 2014 Dmitry Falko <dfalko@digiflak.com>, digiFLAK
 * Fixed by Igor Zhbanov <igor.zhbanov@jolla.com>
 *
 * based on libattr code, original copyright:
 * Copyright (C) 1999-2005 by Erik Andersen <andersen@codepoet.org>
 *
 * Licensed under GPLv2 or later, see file LICENSE in this source tree.
 */

#include <sys/types.h>
#include <sys/xattr.h>

#include "libbb.h"

#if !defined(ENOTSUP)
# define ENOTSUP (-1)
#endif

#if defined(HAVE_ALLOCA)
# define bb_alloc(size) alloca (size)
# define bb_free(ptr) do { } while(0)
#else
# define bb_alloc(size) xmalloc (size)
# define bb_free(ptr) free (ptr)
#endif

/* Copy extended attributes from src_path to dst_path. If the file
 * has an extended Access ACL (system.posix_acl_access) and that is
 * copied successfully, the file mode permission bits are copied as
 * a side effect. This may not always the case, so the file mode
 * and/or ownership must be copied separately. */
int FAST_FUNC copy_file_attr(const char *src_path, const char *dst_path)
{
	int ret = 0;
	ssize_t size;
	char *names = NULL, *end_names, *name, *value = NULL;
	unsigned int setxattr_ENOTSUP = 0;

	if ((size = listxattr(src_path, NULL, 0)) < 0) {
		if (errno != ENOSYS && errno != ENOTSUP) {
			bb_perror_msg("listing attributes of %s", src_path);
			ret = -1;
		}

		goto getout;
	}

	if (!(names = (char *)bb_alloc(size + 1))) {
		bb_error_msg("cannot allocate buffer");
		ret = -1;
		goto getout;
	}

	if ((size = listxattr(src_path, names, size)) < 0) {
		bb_error_msg("listing attributes of %s", src_path);
		ret = -1;
		goto getout;
	} else {
		names[size] = '\0';
		end_names = names + size;
	}

	for (name = names; name != end_names; name = strchr(name, '\0') + 1) {
		void *old_value;

		if (!*name)
			continue;

		if ((size = getxattr(src_path, name, NULL, 0)) < 0) {
			bb_error_msg("getting attribute %s of %s",
				     src_path, name);
			ret = -1;
			continue;
		}

		value = (char *)xrealloc(old_value = value, size);
		if (size != 0 && !value) {
			free(old_value);
			bb_error_msg("failed to realloc");
			ret = -1;
		}

		if ((size = getxattr(src_path, name, value, size)) < 0) {
			bb_error_msg("getting attribute %s of %s",
				     src_path, name);
			ret = -1;
			continue;
		}

		if (setxattr(dst_path, name, value, size, 0) != 0) {
			if (errno == ENOTSUP)
				setxattr_ENOTSUP++;
			else {
				if (errno == ENOSYS) {
					bb_error_msg("setting attributes for "
						     "%s", dst_path);
					ret = -1;
					/* no hope of getting any further */
					break;
				} else {
					bb_error_msg("setting attribute %s "
						     "for %s", name,
						     dst_path);
					ret = -1;
				}
			}
		}
	}

	if (setxattr_ENOTSUP) {
		errno = ENOTSUP;
		/* ignore this error */
		bb_error_msg("setting attributes for %s", dst_path);
		ret = 0;
	}

getout:
	free(value);
	bb_free(names);
	return ret;
}
