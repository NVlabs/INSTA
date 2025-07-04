// graph-tool -- a general graph modification and manipulation thingy
//
// Copyright (C) 2006-2024 Tiago de Paula Peixoto <tiago@skewed.de>
//
// This program is free software; you can redistribute it and/or modify it under
// the terms of the GNU Lesser General Public License as published by the Free
// Software Foundation; either version 3 of the License, or (at your option) any
// later version.
//
// This program is distributed in the hope that it will be useful, but WITHOUT
// ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
// FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
// details.
//
// You should have received a copy of the GNU Lesser General Public License
// along with this program. If not, see <http://www.gnu.org/licenses/>.

#ifndef GRAPH_EXCEPTIONS_HH
#define GRAPH_EXCEPTIONS_HH
#include "config.h"
#include <string>

// Exceptions
// ==========
//
// This is the main exception which will be thrown the outside world, when
// things go wrong

namespace graph_tool{

class GraphException : public std::exception
{
public:
    GraphException(const std::string& error);
    virtual ~GraphException() throw ();
    virtual const char * what () const throw ();
protected:
    std::string _error;
};

class IOException : public GraphException
{
public:
    IOException(const std::string& error);
    virtual ~IOException() throw ();
};

class ValueException : public GraphException
{
public:
    ValueException(const std::string& error);
    virtual ~ValueException() throw ();
};

} // namespace std

#endif // GRAPH_EXCEPTIONS_HH
